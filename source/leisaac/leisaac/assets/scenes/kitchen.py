from pathlib import Path

import isaaclab.sim as sim_utils
from isaaclab.assets import AssetBaseCfg
from leisaac.utils.constant import ASSETS_ROOT

"""Configuration for the Kitchen Scene"""
SCENES_ROOT = Path(ASSETS_ROOT) / "scenes"

KITCHEN_WITH_ORANGE_USD_PATH = str(SCENES_ROOT / "kitchen_with_orange" / "scene.usd")

# Isaac Sim 6.x cannot cook these bodies' collision meshes; the shapeless bodies get degenerate
# transforms that corrupt every RTX camera image after the first physics step.
KITCHEN_WITH_ORANGE_SHAPELESS_BODIES = [
    f"Scene/{name}/_body_0/object"
    for name in ("outlet_room", "outlet_2_room", "light_switch_room", "light_switch_2_room")
]


def spawn_kitchen_with_orange(prim_path, cfg, *args, **kwargs):
    prim = sim_utils.spawn_from_usd(prim_path, cfg, *args, **kwargs)
    stage = sim_utils.get_current_stage()
    for scene_prim in sim_utils.find_matching_prims(prim_path):
        for body_path in KITCHEN_WITH_ORANGE_SHAPELESS_BODIES:
            body = stage.GetPrimAtPath(f"{scene_prim.GetPath()}/{body_path}")
            if body.IsValid():
                body.SetActive(False)
    return prim


KITCHEN_WITH_ORANGE_CFG = AssetBaseCfg(
    spawn=sim_utils.UsdFileCfg(
        func=spawn_kitchen_with_orange,
        usd_path=KITCHEN_WITH_ORANGE_USD_PATH,
    )
)

KITCHEN_WITH_HAMBURGER_USD_PATH = str(SCENES_ROOT / "kitchen_with_hamburger" / "scene.usd")

KITCHEN_WITH_HAMBURGER_CFG = AssetBaseCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=KITCHEN_WITH_HAMBURGER_USD_PATH,
    )
)
