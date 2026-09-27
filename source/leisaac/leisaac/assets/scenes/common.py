import isaaclab.sim as sim_utils


def deactivate_zero_scale_rigid_bodies(prim_path: str) -> list[str]:
    """Deactivate rigid bodies whose world transform has zero scale.

    Some scene USDs hide objects by scaling them to zero while keeping a dynamic rigid body with collision.
    Isaac Sim 6.x cannot cook such geometry; the body gets degenerate transforms that corrupt RTX camera images.
    """
    from pxr import Usd, UsdGeom, UsdPhysics

    stage = sim_utils.get_current_stage()
    deactivated = []
    for root in sim_utils.find_matching_prims(prim_path):
        for prim in Usd.PrimRange(root):
            if not prim.HasAPI(UsdPhysics.RigidBodyAPI):
                continue
            matrix = UsdGeom.Xformable(prim).ComputeLocalToWorldTransform(Usd.TimeCode.Default())
            if abs(matrix.ExtractRotationMatrix().GetDeterminant()) < 1e-12:
                deactivated.append(str(prim.GetPath()))
    for path in deactivated:
        stage.GetPrimAtPath(path).SetActive(False)
    if deactivated:
        print(f"[leisaac] Deactivated {len(deactivated)} zero-scale rigid bodies under {prim_path}")
    return deactivated


def spawn_scene_from_usd(prim_path, cfg, *args, **kwargs):
    prim = sim_utils.spawn_from_usd(prim_path, cfg, *args, **kwargs)
    deactivate_zero_scale_rigid_bodies(prim_path)
    return prim
