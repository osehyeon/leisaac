from pathlib import Path

import isaaclab.sim as sim_utils
from isaaclab.assets import AssetBaseCfg
from leisaac.utils.constant import ASSETS_ROOT

from .common import spawn_scene_from_usd

"""Configuration for the Toy Room Scene"""
SCENES_ROOT = Path(ASSETS_ROOT) / "scenes"

LIGHTWHEEL_BEDROOM_USD_PATH = str(SCENES_ROOT / "lightwheel_bedroom" / "scene.usd")

LIGHTWHEEL_BEDROOM_CFG = AssetBaseCfg(
    spawn=sim_utils.UsdFileCfg(
        func=spawn_scene_from_usd,
        usd_path=LIGHTWHEEL_BEDROOM_USD_PATH,
    )
)
