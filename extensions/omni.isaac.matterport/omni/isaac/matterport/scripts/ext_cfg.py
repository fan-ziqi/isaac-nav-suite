"""
@author     Pascal Roth
@email      rothpa@student.ethz.ch

@brief      Config for MatterPort3D Extension in Omniverse-Isaac Sim
"""

# python
from dataclasses import dataclass
from omni.isaac.matterport.config.importer_cfg import MatterportImporterCfg


@dataclass
class MatterportExtConfig:
    # config classes
    importer: MatterportImporterCfg = MatterportImporterCfg()
    # semantic and depth inforamtion (can be changed individually for each camera)
    visualize: bool = False
    visualize_prim: str = None

    # set value functions
    def set_friction_dynamic(self, value: float):
        self.importer.physics_material.dynamic_friction = value

    def set_friction_static(self, value: float):
        self.importer.physics_material.static_friction = value

    def set_restitution(self, value: float):
        self.importer.physics_material.restitution = value

    def set_friction_combine_mode(self, value: int):
        self.importer.physics_material.friction_combine_mode = value

    def set_restitution_combine_mode(self, value: int):
        self.importer.physics_material.restitution_combine_mode = value

    def set_improved_patch_friction(self, value: bool):
        self.importer.physics_material.improve_patch_friction = value

    def set_obj_filepath(self, value: str):
        self.importer.obj_filepath = value

    def set_prim_path(self, value: str):
        self.importer.prim_path = value

    def set_visualize(self, value: bool):
        self.visualize = value

    def set_visualization_prim(self, value: str):
        self.visualize_prim = value