# Copyright (c) 2024 Ziqi Fan
# Author: Ziqi Fan
# All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

import sys

import open3d as o3d

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename.ply>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        pcd = o3d.io.read_point_cloud(file_path)
        print(f"Successfully loaded point cloud: {file_path}")
    except Exception as e:
        print(f"Error reading the file {file_path}: {e}")
        sys.exit(1)

    o3d.visualization.draw_geometries([pcd])
