# Copyright (c) 2024 Ziqi Fan
# Author: Ziqi Fan
# All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0

import os
import sys


def add_prefix_suffix(directory, prefix="", suffix=""):
    for filename in os.listdir(directory):
        name, ext = os.path.splitext(filename)
        new_filename = prefix + name + suffix + ext
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python script.py <directory> [prefix] [suffix]")
        sys.exit(1)

    directory = sys.argv[1]
    prefix = sys.argv[2] if len(sys.argv) > 2 else ""
    suffix = sys.argv[3] if len(sys.argv) > 3 else ""

    add_prefix_suffix(directory, prefix, suffix)
