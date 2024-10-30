# Copyright (c) 2024 ETH Zurich (Robotic Systems Lab)
# Author: Pascal Roth, Ziqi Fan
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""
This script demonstrates how to use the rigid objects class.
"""

"""Launch Isaac Sim Simulator first."""

import argparse

# omni-isaac-orbit
from omni.isaac.lab.app import AppLauncher

# add argparse arguments
parser = argparse.ArgumentParser(description="This script demonstrates how to use the camera sensor.")
parser.add_argument("--headless", action="store_true", default=False, help="Force display off at all times.")
parser.add_argument("--num_envs", type=int, default=1, help="Number of environments to spawn.")
args_cli = parser.parse_args()
args_cli.enable_cameras = True

# launch omniverse app
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

"""Rest everything follows."""
import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.sim import SimulationContext
from omni.viplanner.collectors.collectors import (
    CarlaSceneCfg,
    ViewpointSampling,
    ViewpointSamplingCfg,
)
from omni.viplanner.collectors.configs import CarlaSemanticCostMapping

SAVE_PATH = ""

"""
Main
"""


def main():
    """Main function."""
    # Load kit helper
    sim_cfg = sim_utils.SimulationCfg()
    sim = SimulationContext(sim_cfg)
    # Set main camera
    sim.set_camera_view([130, -125, 30], [100, -130, 0.5])

    cfg = ViewpointSamplingCfg()
    cfg.exploration_scene = CarlaSceneCfg(args_cli.num_envs, env_spacing=1.0)
    # overwrite semantic cost mapping and adjust parameters based on larger map
    cfg.terrain_analysis.semantic_cost_mapping = CarlaSemanticCostMapping()
    cfg.terrain_analysis.grid_resolution = 1.0
    cfg.terrain_analysis.sample_points = 10000
    # limit space to be within the road network
    cfg.terrain_analysis.dim_limiter_prim = "Road_Sidewalk"
    # enable debug visualization
    cfg.terrain_analysis.viz_graph = True
    cfg.save_path = SAVE_PATH

    explorer = ViewpointSampling(cfg)
    # Now we are ready!
    print("[INFO]: Setup complete...")

    # sample and render viewpoints
    samples = explorer.sample_viewpoints(5000)
    explorer.render_viewpoints(samples)
    print(
        "[INFO]: Viewpoints sampled and rendered will continue to render the environment and visualize the last camera"
        " positions..."
    )

    # Define simulation stepping
    sim_dt = sim.get_physics_dt()
    # Simulation loop
    while simulation_app.is_running():
        # Perform step
        sim.render()
        # Update buffers
        explorer.scene.update(sim_dt)


if __name__ == "__main__":
    # Run the main function
    main()
    # Close the simulator
    simulation_app.close()
