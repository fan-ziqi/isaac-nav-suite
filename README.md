<div style="display: flex;">
    <img src="docs/example_matterport.png" alt="Matterport Mesh" style="width: 48%; padding: 5px;">
    <img src="docs/example_carla.png" alt="Unreal Engine / Carla Mesh" style="width: 48%; padding: 5px;">
</div>

---

# Omniverse Matterport3D and Unreal Engine Assets Extensions

[![IsaacSim](https://img.shields.io/badge/IsaacSim-2023.1.0--hotfix.1-silver.svg)](https://docs.omniverse.nvidia.com/isaacsim/latest/overview.html)
[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://docs.python.org/3/whatsnew/3.10.html)
[![Linux platform](https://img.shields.io/badge/platform-linux--64-orange.svg)](https://releases.ubuntu.com/20.04/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![License](https://img.shields.io/badge/license-BSD--3-yellow.svg)](https://opensource.org/licenses/BSD-3-Clause)

This repository contains the extensions for Matterport3D and Unreal Engine Assets.
The extensions enable the easy loading of assets into Isaac Sim and have access to the semantic labels.
They are developed as part of the ViPlanner project ([Paper](https://arxiv.org/abs/2310.00982) | [Code](https://github.com/leggedrobotics/viplanner))
and are based on the [IsaacLab](https://isaac-sim.github.io/IsaacLab/) framework.

**Attention:**
The central part of the extensions is currently updated to the latest IsaacLab version.
This repo contains a temporary solution sufficient for the demo script included in ViPlanner, found [here](https://github.com/leggedrobotics/viplanner/tree/main/omniverse).
An updated version will be available soon.


## Installation

To install the extensions, follow these steps:

1. Install Isaac Sim using the [IsaacLab installation guide](https://isaac-sim.github.io/IsaacLab/source/setup/installation/index.html).
2. Clone the IsaacLab repo and run the installer script.

```
git clone git@github.com:isaac-sim/IsaacLab.git
cd IsaacLab
./isaaclab.sh -i
```

3. Then install extensions.

```
./isaaclab.sh -p  -m pip install -e ./extensions/omni.isaac.matterport
./isaaclab.sh -p  -m pip install -e ./extensions/omni.isaac.carla
```

## Usage

For the Matterport extension, a GUI interface is available. To use it, start the simulation:

```
./isaaclab.sh -s
```

Then, in the GUI, go to `Window -> Extensions` and type `Matterport` in the search bar. You should see the Matterport3D extension.
Enable it to open the GUI interface.

To use both as part of an IsaacLab workflow, please refer to the [ViPlanner Demo](https://github.com/leggedrobotics/viplanner/tree/main/omniverse).


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
