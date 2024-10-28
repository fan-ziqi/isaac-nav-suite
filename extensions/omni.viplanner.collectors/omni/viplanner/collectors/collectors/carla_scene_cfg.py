import os

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.assets import AssetBaseCfg
from omni.isaac.lab.scene import InteractiveSceneCfg
from omni.isaac.lab.sensors import CameraCfg
from omni.isaac.lab.utils import configclass
from omni.viplanner.importer.importer import UnRealImporterCfg
from omni.viplanner.importer.sensors import DATA_DIR


USD_PATH = ""

@configclass
class CarlaSceneCfg(InteractiveSceneCfg):
    """Configuration for a carla scene with a camera."""

    # ground terrain
    terrain = UnRealImporterCfg(
        prim_path="/World/Carla",
        physics_material=sim_utils.RigidBodyMaterialCfg(
            friction_combine_mode="multiply",
            restitution_combine_mode="multiply",
            static_friction=1.0,
            dynamic_friction=1.0,
        ),
        usd_path=USD_PATH,
        duplicate_cfg_file=[
            os.path.join(DATA_DIR, "unreal", "town01", "cw_multiply_cfg.yml"),
            os.path.join(DATA_DIR, "unreal", "town01", "vehicle_cfg.yml"),
        ],
        sem_mesh_to_class_map=os.path.join(DATA_DIR, "unreal", "town01", "keyword_mapping.yml"),
        people_config_file=os.path.join(DATA_DIR, "unreal", "town01", "people_cfg.yml"),
    )
    # camera
    camera_0 = CameraCfg(
        prim_path="{ENV_REGEX_NS}/sem_cam",
        update_period=0,
        data_types=["semantic_segmentation"],
        debug_vis=True,
        offset=CameraCfg.OffsetCfg(pos=(0.419, -0.025, -0.020), rot=(0.992, 0.008, 0.127, 0.001), convention="world"),
        height=720,
        width=1280,
        spawn=sim_utils.PinholeCameraCfg(
            focal_length=24,
            horizontal_aperture=20.955,
        ),
    )
    camera_1 = CameraCfg(
        prim_path="{ENV_REGEX_NS}/depth_cam",
        update_period=0,
        data_types=["distance_to_image_plane"],
        debug_vis=False,
        offset=CameraCfg.OffsetCfg(pos=(0.419, -0.025, -0.020), rot=(0.992, 0.008, 0.127, 0.001), convention="world"),
        height=480,
        width=848,
        spawn=sim_utils.PinholeCameraCfg(
            focal_length=24,
            horizontal_aperture=20.955,
        ),
    )
    # extras - light
    light = AssetBaseCfg(
        prim_path="/World/light",
        spawn=sim_utils.DistantLightCfg(intensity=3000.0, color=(0.75, 0.75, 0.75)),
        init_state=AssetBaseCfg.InitialStateCfg(pos=(0.0, 0.0, 500.0)),
    )
