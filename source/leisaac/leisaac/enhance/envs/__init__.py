from . import mdp
from .direct_rl_env_cfg import RecorderEnhanceDirectRLEnvCfg
from .manager_based_rl_digital_twin_env_cfg import ManagerBasedRLDigitalTwinEnvCfg

_LAZY_IMPORTS = {
    "RecorderEnhanceDirectRLEnv": ".direct_rl_env",
    "ManagerBasedRLDigitalTwinEnv": ".manager_based_rl_digital_twin_env",
    "ManagerBasedRLLeIsaacMimicEnv": ".manager_based_rl_leisaac_mimic_env",
}


def __getattr__(name):
    # env classes cannot be imported before Kit starts
    if name not in _LAZY_IMPORTS:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    from importlib import import_module

    value = getattr(import_module(_LAZY_IMPORTS[name], __name__), name)
    globals()[name] = value
    return value
