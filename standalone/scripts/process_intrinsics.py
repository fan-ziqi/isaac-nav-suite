# Copyright (c) 2024 Ziqi Fan
# Author: Ziqi Fan
# All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

import os
import sys

import numpy as np


def process_intrinsics_file(file_path):
    K = np.zeros((3, 3))

    with open(file_path) as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        values = line.strip().split(",")
        K[i, :] = list(map(float, values))

    P = np.zeros((3, 4))
    P[:3, :3] = K

    base_name, ext = os.path.splitext(file_path)
    output_file = base_name + "_p" + ext

    flat_P = P.flatten()
    with open(output_file, "w") as f:
        f.write(",".join(map(str, flat_P)) + "\n")

    print(f"Projection matrix P saved to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <intrinsics.txt>")
        sys.exit(1)

    file_path = sys.argv[1]

    process_intrinsics_file(file_path)
