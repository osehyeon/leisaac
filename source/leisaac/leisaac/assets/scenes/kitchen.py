from pathlib import Path

import isaaclab.sim as sim_utils
from isaaclab.assets import AssetBaseCfg
from leisaac.utils.constant import ASSETS_ROOT

from .common import spawn_scene_from_usd

"""Configuration for the Kitchen Scene"""
SCENES_ROOT = Path(ASSETS_ROOT) / "scenes"

KITCHEN_WITH_ORANGE_USD_PATH = str(SCENES_ROOT / "kitchen_with_orange" / "scene.usd")

KITCHEN_WITH_ORANGE_CFG = AssetBaseCfg(
    spawn=sim_utils.UsdFileCfg(
        func=spawn_scene_from_usd,
        usd_path=KITCHEN_WITH_ORANGE_USD_PATH,
    )
)

KITCHEN_WITH_HAMBURGER_USD_PATH = str(SCENES_ROOT / "kitchen_with_hamburger" / "scene.usd")

KITCHEN_WITH_HAMBURGER_CFG = AssetBaseCfg(
    spawn=sim_utils.UsdFileCfg(
        func=spawn_scene_from_usd,
        usd_path=KITCHEN_WITH_HAMBURGER_USD_PATH,
    )
)
