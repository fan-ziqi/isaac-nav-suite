"""Installation script for the 'omni.isaac.matterport' python package."""


from setuptools import setup

# Minimum dependencies required prior to installation
INSTALL_REQUIRES = [
    # generic
    "trimesh",
    "opencv-python-headless",
    "open3d",
    "PyQt5",
]

# Installation operation
setup(
    name="omni-isaac-matterport",
    author="Pascal Roth",
    author_email="rothpa@student.ethz.ch",
    version="0.0.1",
    description="Extension to include Matterport 3D Datasets into Isaac (taken from https://niessner.github.io/Matterport/).",
    keywords=["robotics"],
    include_package_data=True,
    python_requires="==3.7.*",
    install_requires=INSTALL_REQUIRES,
    packages=["omni.isaac.matterport"],
    classifiers=["Natural Language :: English", "Programming Language :: Python :: 3.7"],
    zip_safe=False,
)

# EOF