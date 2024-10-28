# Copyright (c) 2024 ETH Zurich (Robotic Systems Lab)
# Author: Pascal Roth
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import omni.isaac.lab.sim as sim_utils
import torch
from omni.isaac.lab.scene import InteractiveSceneCfg
from omni.isaac.lab.sensors import patterns
from omni.isaac.lab.utils import configclass

from .terrain_analysis_cfg import TerrainAnalysisCfg


@configclass
class ExplorationCfg:
    # scene and import definition
    sim: sim_utils.SimulationCfg = sim_utils.SimulationCfg()
    exploration_scene: InteractiveSceneCfg = None
    """Parameters to construct the matterport scene"""
    terrain_analysis: TerrainAnalysisCfg = TerrainAnalysisCfg(raycaster_sensor="camera_0")
    """Name of the camera object in the scene definition used for the terrain analysis."""

    # sampling
    sample_points: int = 10000
    """Number of random points to sample."""
    x_angle_range: tuple[float, float] = (-2.5, 2.5)
    y_angle_range: tuple[float, float] = (-2, 5)  # negative angle means in isaac convention: look down
    """Range of the x and y angle of the camera (in degrees), will be randomly selected according to a uniform distribution"""
    height: float = 0.5
    """Height to use for the random points."""

    # point filtering
    min_height: float = 0.2
    """Maximum height to be considered an accessible point for the robot"""
    ground_height: float = -0.1
    """Height of the ground plane"""
    min_wall_distance: float = 0.5
    """Minimum distance to a wall to be considered an accessible point for the robot"""
    min_hit_rate: float = 0.8
    """Don't use a point if the hit rate is below this value"""
    min_avg_hit_distance: float = 0.5
    """Don't use a point if the max hit distance is below this value"""
    min_std_hit_distance: float = 0.5
    """Don't use a point if the std hit distance is below this value"""

    # convergence
    conv_rate: float = 0.9
    """Rate of faces that are covered by three different images, used to terminate the exploration"""

    device = "cuda" if torch.cuda.is_available() else "cpu"
    """Device to use for computations."""
