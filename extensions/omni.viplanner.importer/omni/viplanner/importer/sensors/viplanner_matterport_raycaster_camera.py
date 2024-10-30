# Copyright (c) 2024 Ziqi Fan
# Author: Ziqi Fan
# All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

import torch
import yaml
from omni.viplanner.collectors.configs.viplanner_sem_meta import VIPlannerSemMetaHandler
from omni.viplanner.importer.sensors import DATA_DIR

from .matterport_raycaster_camera import MatterportRayCasterCamera


class VIPlannerMatterportRayCasterCamera(MatterportRayCasterCamera):
    def __init__(self, cfg: object):
        super().__init__(cfg)

    def _color_mapping(self):
        viplanner_sem = VIPlannerSemMetaHandler()
        with open(DATA_DIR + "/matterport/mpcat40_to_vip_sem.yml") as file:
            map_mpcat40_to_vip_sem = yaml.safe_load(file)
        color = viplanner_sem.get_colors_for_names(list(map_mpcat40_to_vip_sem.values()))
        self.color = torch.tensor(color, device=self._device, dtype=torch.uint8)
