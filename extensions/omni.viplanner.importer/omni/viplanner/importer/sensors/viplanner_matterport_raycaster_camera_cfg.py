# Copyright (c) 2024 Ziqi Fan
# Author: Ziqi Fan
# All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

from omni.isaac.lab.sensors.ray_caster import RayCasterCameraCfg
from omni.isaac.lab.utils import configclass

from .viplanner_matterport_raycaster_camera import VIPlannerMatterportRayCasterCamera


@configclass
class VIPlannerMatterportRayCasterCameraCfg(RayCasterCameraCfg):
    """Configuration for the ray-cast camera for Matterport Environments."""

    class_type = VIPlannerMatterportRayCasterCamera
    """Name of the specific matterport ray caster camera class."""
