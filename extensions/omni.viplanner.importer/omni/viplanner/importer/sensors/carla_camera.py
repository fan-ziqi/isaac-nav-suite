# Copyright (c) 2024 Ziqi Fan
# Author: Ziqi Fan
# All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import torch
from omni.isaac.lab.sensors import Camera
from omni.isaac.lab.utils.array import convert_to_torch
from omni.viplanner.collectors.configs.viplanner_sem_meta import VIPlannerSemMetaHandler

if TYPE_CHECKING:
    from .carla_camera_cfg import VIPlannerCarlaCameraCfg

# initialize viplanner config
VIPLANNER_SEM_META = VIPlannerSemMetaHandler()


class VIPlannerCarlaCamera(Camera):

    cfg: VIPlannerCarlaCameraCfg

    def _process_annotator_output(self, name: str, output: Any) -> tuple[torch.tensor, dict | None]:
        """Process the annotator output.

        This function is called after the data has been collected from all the cameras.
        """
        # extract info and data from the output
        if isinstance(output, dict):
            data = output["data"]
            info = output["info"]
        else:
            data = output
            info = None
        # convert data into torch tensor
        data = convert_to_torch(data, device=self.device)

        # process data for different segmentation types
        # Note: Replicator returns raw buffers of dtype int32 for segmentation types
        #   so we need to convert them to uint8 4 channel images for colorized types
        height, width = self.image_shape
        if name == "semantic_segmentation":
            info = info["idToLabels"]
            # assign each key a color from the VIPlanner color space
            info = {
                int(k): (
                    VIPLANNER_SEM_META.class_color["static"]
                    if v["class"] in ("BACKGROUND", "UNLABELLED")
                    else VIPLANNER_SEM_META.class_color[v["class"]]
                )
                for k, v in info.items()
            }
            # create recolored images
            output = torch.zeros((*data.shape[:3], 3), device=self.device, dtype=torch.uint8)
            # NOTE: the label_ids and the ids in the data might not be the same, label ids might not be continuous and
            #       might not start from 0 as well as some data ids might not be present in the label ids
            unique_data_ids = torch.unique(data).sort()[0]
            mapping = torch.zeros(
                (max(unique_data_ids.max() + 1, max(info.keys()) + 1), 3), dtype=torch.uint8, device=self.device
            )
            mapping[list(info.keys())] = torch.tensor(list(info.values()), dtype=torch.uint8, device=self.device)
            output = mapping[data.long().squeeze(-1)]
            if self.cfg.colorize_semantic_segmentation:
                data = data.view(torch.uint8).reshape(height, width, -1)
            else:
                data = output
        elif name == "instance_segmentation_fast":
            if self.cfg.colorize_instance_segmentation:
                data = data.view(torch.uint8).reshape(height, width, -1)
            else:
                data = data.view(height, width, 1)
        elif name == "instance_id_segmentation_fast":
            if self.cfg.colorize_instance_id_segmentation:
                data = data.view(torch.uint8).reshape(height, width, -1)
            else:
                data = data.view(height, width, 1)
        # make sure buffer dimensions are consistent as (H, W, C)
        elif name == "distance_to_camera" or name == "distance_to_image_plane" or name == "depth":
            data = data.view(height, width, 1)
        # we only return the RGB channels from the RGBA output if rgb is required
        # normals return (x, y, z) in first 3 channels, 4th channel is unused
        elif name == "rgb" or name == "normals":
            data = data[..., :3]
        # motion vectors return (x, y) in first 2 channels, 3rd and 4th channels are unused
        elif name == "motion_vectors":
            data = data[..., :2]

        # return the data and info
        return data, info
