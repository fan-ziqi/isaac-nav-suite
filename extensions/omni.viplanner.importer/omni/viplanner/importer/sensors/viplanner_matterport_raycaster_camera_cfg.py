# Copyright (c) 2024 ETH Zurich (Robotic Systems Lab)
# Author: Pascal Roth
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from omni.isaac.lab.sensors.ray_caster import RayCasterCameraCfg
from omni.isaac.lab.utils import configclass

from .viplanner_matterport_raycaster_camera import VIPlannerMatterportRayCasterCamera


@configclass
class VIPlannerMatterportRayCasterCameraCfg(RayCasterCameraCfg):
    """Configuration for the ray-cast camera for Matterport Environments."""

    class_type = VIPlannerMatterportRayCasterCamera
    """Name of the specific matterport ray caster camera class."""
