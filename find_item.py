"""Find item."""

from icecream import ic

from artifactsmmo_sdk import ArtifactsClient
from artifactsmmo_sdk.models.items import ItemSchema

guile = ArtifactsClient()


def find_item_map(item: ItemSchema):
    """Find item on the map."""
    if item.type == "resource" and item.subtype == "mob":
        monster = guile.monsters.get_all_monsters(
            drop=item.code,
            max_level=item.level,
            min_level=item.level,
        ).data
        ic(monster)

        maps = guile.maps.get_all_maps(
            content_code=monster[0].code,
            content_type="monster",
        ).data
        ic(maps)

    elif item.type == "resource" and item.subtype in [
        "mining",
        "woodcutting",
        "fishing",
    ]:
        resource = guile.resources.get_all_resources(
            drop=item.code,
            max_level=item.level,
            min_level=item.level,
            skill=item.subtype,
        ).data
        ic(resource)

        maps = guile.maps.get_all_maps(
            content_code=resource[0].code,
            content_type="resource",
        ).data
        ic(maps)
    else:
        ic(item)


if __name__ == "__main__":
    item1 = guile.items.get_item(code="feather").data.item
    find_item_map(item=item1)

    item2 = guile.items.get_item(code="copper_ore").data.item
    find_item_map(item=item2)

    item3 = guile.items.get_item(code="ash_plank").data.item
    find_item_map(item=item3)
