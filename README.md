# viplanner_data_generator

**viplanner_data_generator** can generator data for the ViPlanner project. It provides tools to collect and sample viewpoints from Matterport and Carla.

The current version was developed as part of the ViPlanner project ([Paper](https://arxiv.org/abs/2310.00982) | [Code](https://github.com/leggedrobotics/viplanner))
and are based on the [IsaacLab](https://isaac-sim.github.io/IsaacLab) framework.

## Installation

1. Install Isaac Sim using the [IsaacLab installation guide](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html).

```bash
git clone git@github.com:isaac-sim/IsaacLab.git
git clone git@github.com:fan-ziqi/viplanner_data_generator.git
```

2. Link the extensions into the IsaacLab extension directory

```bash
cd <path-to-your-IsaacLab-repo>/source/extensions
ln -s <path-to-your-viplanner-data-generator-repo>/extensions/omni.viplanner.importer .
ln -s <path-to-your-viplanner-data-generator-repo>/extensions/omni.viplanner.collector .
```

3. Then run the IsaacLab installer script.

```bash
cd <path-to-your-IsaacLab-repo>
./isaaclab.sh -i
```

## Usage

Standalone scripts can be used to custmize the functionalities and easily integrate different parts of the extensions for your own projects.
Here we provide a set of examples that demonstrate how to use the different parts:

**You need to search and modify the `USD_PATH`, `PLY_PATH` and `SAVE_PATH` in the code. All require an absolute path.**

  - Sample Trajectories from Matterport:
    ```
    python standalone/omni.viplanner.collectors/check_matterport_trajectory_sampling.py
    ```
  - Sample Trajectories from Carla (Unreal Engine):
    ```
    python standalone/omni.viplanner.collectors/check_carla_trajectory_sampling.py
    ```
  - Sample Viewpoints and Render Images from Matterport:
    ```
    python standalone/omni.viplanner.collectors/check_matterport_viewpoint_sampling.py
    ```
  - Sample Viewpoints and Render Images from Carla (Unreal Engine):
    ```
    python standalone/omni.viplanner.collectors/check_carla_viewpoint_sampling.py
    ```

## <a name="CitingViPlanner"></a>Citing

If you use this code in a scientific publication, please cite the following [paper](https://arxiv.org/abs/2310.00982):
```
@article{roth2023viplanner,
  title     ={ViPlanner: Visual Semantic Imperative Learning for Local Navigation},
  author    ={Pascal Roth and Julian Nubert and Fan Yang and Mayank Mittal and Marco Hutter},
  journal   = {2024 IEEE International Conference on Robotics and Automation (ICRA)},
  year      = {2023},
  month     = {May},
}
```

### License

This code belongs to the Robotic Systems Lab, ETH Zurich.
All right reserved

**Authors: [Pascal Roth](https://github.com/pascal-roth), [Ziqi Fan](https://github.com/fan-ziqi)<br />
Maintainer: Pascal Roth, rothpa@ethz.ch**

This repository contains research code, except that it changes often, and any fitness for a particular purpose is disclaimed.
