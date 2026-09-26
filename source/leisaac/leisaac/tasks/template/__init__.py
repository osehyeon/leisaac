from .bi_arm_env_cfg import (
    BiArmObservationsCfg,
    BiArmTaskEnvCfg,
    BiArmTaskSceneCfg,
    BiArmTerminationsCfg,
)
from .lekiwi_env_cfg import (
    LeKiwiActionsCfg,
    LeKiwiEventCfg,
    LeKiwiObservationsCfg,
    LeKiwiRewardsCfg,
    LeKiwiTaskEnvCfg,
    LeKiwiTaskSceneCfg,
    LeKiwiTerminationsCfg,
)
from .single_arm_env_cfg import (
    SingleArmObservationsCfg,
    SingleArmTaskEnvCfg,
    SingleArmTaskSceneCfg,
    SingleArmTerminationsCfg,
)

_LAZY_IMPORTS = {
    "BiArmTaskDirectEnv": ".direct.bi_arm_env",
    "BiArmTaskDirectEnvCfg": ".direct.bi_arm_env",
    "SingleArmTaskDirectEnv": ".direct.single_arm_env",
    "SingleArmTaskDirectEnvCfg": ".direct.single_arm_env",
}


def __getattr__(name):
    # direct envs subclass DirectRLEnv, which cannot be imported before Kit starts
    if name not in _LAZY_IMPORTS:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    from importlib import import_module

    value = getattr(import_module(_LAZY_IMPORTS[name], __name__), name)
    globals()[name] = value
    return value
