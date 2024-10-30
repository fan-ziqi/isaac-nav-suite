# Copyright (c) 2024 Ziqi Fan
# Author: Ziqi Fan
# All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

from omni.isaac.lab.sensors import CameraCfg
from omni.isaac.lab.utils import configclass

from .carla_camera import VIPlannerCarlaCamera


@configclass
class VIPlannerCarlaCameraCfg(CameraCfg):
    """Configuration for a camera sensor."""

    class_type: type = VIPlannerCarlaCamera
