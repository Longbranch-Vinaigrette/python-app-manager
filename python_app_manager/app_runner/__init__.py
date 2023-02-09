import os.path
import subprocess

from ..packages import Packages


def check_and_run_pipenv(path):
    """Check if the app uses pipenv and run the app

    :returns True if it was successful"""
    if os.path.exists(f"{path}{os.path.sep}Pipfile"):

        # If the user doesn't have pipenv but the file Pipfile exists
        # in the folder, we can install it.
        pkgs = Packages()
        result = pkgs.find("pipenv")

        if not result:
            # "If the package doesn't exist, just install it" - Sigma grindset rule 420
            subprocess.run(["pip3", "install", "pipenv"])

        # Start the actual app
        subprocess.run(["/bin/bash",
                        "-c",
                        # Cd to the given path
                        f"cd {path};"
                        # Normally python projects use main.py to start the app
                        f"pipenv run python main.py;"])
        return True
    else:
        return False
