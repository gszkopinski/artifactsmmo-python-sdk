"""Compare the SDK with the official OpenAPI spec and print the differences.

Usage: uv run python scripts/check_openapi.py [--spec openapi.json]

Checks, per operation: verb+path exists, query/body parameter names, documented
error codes handled, and response model fields. Exit code 1 if any gap.
"""

import argparse
import ast
import json
import re
import sys
import typing
import urllib.request
from pathlib import Path

from pydantic import BaseModel

from artifactsmmo_sdk import ArtifactsClient  # noqa: F401  (imports all models)
from artifactsmmo_sdk import models as _models  # noqa: F401
from artifactsmmo_sdk.base import COMMON_ERRORS

SPEC_URL = "https://api.artifactsmmo.com/openapi.json"
SRC = Path(__file__).parent.parent / "src" / "artifactsmmo_sdk"


def norm(path: str) -> str:
    """Normalise path parameters so names do not matter."""
    return re.sub(r"\{\w+\}", "{}", path)


def load_spec(path: str | None) -> dict:
    if path:
        return json.loads(Path(path).read_text())
    with urllib.request.urlopen(SPEC_URL, timeout=30) as response:
        return json.load(response)


def sdk_calls() -> dict[tuple[str, str], dict]:
    """Parse every `self._request(...)` call of the SDK modules."""
    calls = {}
    for file in SRC.glob("*/*.py"):
        tree = ast.parse(file.read_text())
        for node in ast.walk(tree):
            if not (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "_request"
                and len(node.args) >= 3
            ):
                continue
            verb = ast.literal_eval(node.args[0])
            path = ast.get_source_segment(file.read_text(), node.args[1])
            path = re.sub(r"\{\w+\}", "{}", path.strip("f\"'"))
            schema = ast.unparse(node.args[2])
            errors, params, body = set(), set(), set()
            if len(node.args) > 4 and isinstance(node.args[4], ast.Dict):
                errors = {k.value for k in node.args[4].keys}
            for kw in node.keywords:
                if kw.arg == "params" and isinstance(kw.value, ast.Dict):
                    params = {k.value for k in kw.value.keys}
                if kw.arg == "json" and isinstance(kw.value, ast.Dict):
                    body = {k.value for k in kw.value.keys}
            calls[(verb.upper(), path)] = {
                "schema": schema,
                "errors": errors,
                "params": params,
                "body": body,
                "file": file.relative_to(SRC.parent.parent),
            }
    return calls


def deref(spec: dict, schema: dict) -> dict:
    """Follow $ref and flatten allOf/anyOf/oneOf properties."""
    if "$ref" in schema:
        target = spec
        for part in schema["$ref"].lstrip("#/").split("/"):
            target = target[part]
        return deref(spec, target)
    return schema


def spec_fields(spec: dict, schema: dict) -> dict[str, dict]:
    schema = deref(spec, schema)
    return schema.get("properties", {})


def sdk_models() -> dict[str, type[BaseModel]]:
    found = {}
    for mod in list(sys.modules.values()):
        if mod and getattr(mod, "__name__", "").startswith("artifactsmmo_sdk.models"):
            for name, obj in vars(mod).items():
                if isinstance(obj, type) and issubclass(obj, BaseModel):
                    found[name] = obj
    return found


def inner_model(annotation) -> type[BaseModel] | None:
    """Return the BaseModel hidden in X | None, list[X]..."""
    if isinstance(annotation, type) and issubclass(annotation, BaseModel):
        return annotation
    for arg in typing.get_args(annotation):
        if arg is type(None):
            continue
        found = inner_model(arg)
        if found:
            return found
    return None


def compare_fields(spec, schema: dict, model: type[BaseModel], where: str, out, seen):
    if (where, model) in seen:
        return
    seen.add((where, model))
    props = spec_fields(spec, schema)
    sdk_fields = {f.alias or n for n, f in model.model_fields.items()}
    sdk_fields |= set(model.model_fields)
    for name in props:
        if name not in sdk_fields:
            out.append(f"  model {model.__name__}: field '{name}' missing ({where})")
    for name, field in model.model_fields.items():
        key = field.alias or name
        if props and key not in props and name not in props:
            out.append(
                f"  model {model.__name__}: field '{name}' not in spec ({where})"
            )
            continue
        sub = inner_model(field.annotation)
        if sub and key in props:
            sub_schema = props[key]
            sub_schema = sub_schema.get("items", sub_schema)
            for alt in sub_schema.get("anyOf", []) + sub_schema.get("oneOf", []):
                if alt.get("type") != "null":
                    sub_schema = alt.get("items", alt)
            compare_fields(spec, sub_schema, sub, f"{where}.{key}", out, seen)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec")
    args = parser.parse_args()
    spec = load_spec(args.spec)
    calls = sdk_calls()
    models = sdk_models()
    gaps: list[str] = []
    spec_ops = {}
    for path, item in spec["paths"].items():
        for verb, op in item.items():
            spec_ops[(verb.upper(), norm(path))] = (path, op)

    print(
        f"spec {spec['info']['version']}: {len(spec_ops)} operations, SDK: {len(calls)}"
    )
    for key in sorted(spec_ops.keys() - calls.keys()):
        gaps.append(f"MISSING {key[0]} {spec_ops[key][0]}")
    for key in sorted(calls.keys() - spec_ops.keys()):
        gaps.append(f"NOT IN SPEC {key[0]} {key[1]} ({calls[key]['file']})")

    for key in sorted(calls.keys() & spec_ops.keys()):
        path, op = spec_ops[key]
        call = calls[key]
        out: list[str] = []
        query = {p["name"] for p in op.get("parameters", []) if p["in"] == "query"}
        for name in call["params"] - query:
            out.append(f"  query param '{name}' not in spec")
        for name in query - call["params"]:
            out.append(f"  query param '{name}' not supported")
        body = op.get("requestBody", {}).get("content", {}).get("application/json")
        if body:
            fields = set(spec_fields(spec, body["schema"]))
            for name in call["body"] - fields:
                out.append(f"  body field '{name}' not in spec")
            for name in fields - call["body"]:
                out.append(f"  body field '{name}' not sent")
        documented = {int(c) for c in op["responses"] if c.isdigit() and c != "200"}
        handled = call["errors"] | set(COMMON_ERRORS)
        for code in sorted(documented - handled):
            out.append(f"  error {code} not handled")
        ok = op["responses"].get("200", {}).get("content", {}).get("application/json")
        model = models.get(call["schema"])
        if ok and model:
            compare_fields(spec, ok["schema"], model, call["schema"], out, set())
        elif ok:
            out.append(f"  response model '{call['schema']}' not found")
        if out:
            gaps.append(f"{key[0]} {path} ({call['file']})\n" + "\n".join(out))

    print("\n".join(gaps) if gaps else "No gap.")
    print(f"\n{len(gaps)} operation(s) with gaps")
    return 1 if gaps else 0


if __name__ == "__main__":
    sys.exit(main())
