import os
from setuptools import setup, find_packages
import pathlib

project_path = pathlib.Path(__file__).parent.resolve()

# Load description
with open(f"{project_path}{os.path.sep}README.md") as f:
    description = f.read()

setup(
    name="python-app-manager",
    version="0.0.1",
    description="Pyton app manager",
    long_description=description,
    url="https://github.com/Perseverancia-company/python-app-manager",
    author="Felix Riddle",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="app manager",
    # Only allow versions 0.10.2 and above but not above 1.x.x
    install_requires=["toml>=0.10.2,<1"],
    python_requires="3.10.*",
    package_data={
        "": ["README.md"]
    }
)
