import os
import pprint
import subprocess

import psutil

from .longbranch_vinaigrette_py_gitconfig import Gitconfig
from . import longbranch_vinaigrette_py_process_utils as py_process_utils

from . import app_runner


def setup_submodules(app_path: str):
    """Setup/Install/Update submodules"""
    # Because I like submodules a lot :D
    # Use submodule py_gitconfig to extract data
    gitmodules_path = f"{app_path}{os.path.sep}.gitmodules"
    if os.path.exists(gitmodules_path):
        config = Gitconfig(gitmodules_path)
        gitconfig = config.loads()
    else:
        # The app/repository doesn't have submodules
        return

    # Get submodules paths
    for key in list(gitconfig.keys()):
        # This might not work on windows
        relative_path = f"{gitconfig[key]['path']}"
        submodule_path = f"{app_path}{os.path.sep}{relative_path}"
        is_empty = not os.listdir(submodule_path)

        if is_empty:
            # Install submodules and return
            print("There's a submodule missing, installing every submodule "
                  "in existence...")
            subprocess.run(["/bin/bash",
                            "-c",
                            # Cd our way in
                            f"cd {app_path};"
                            "git submodule update --remote --init --recursive --merge;"])
            return


class PythonAppManager:
    def __init__(self, args=None):
        """Python app manager

        :args Parsed arguments given by the command line"""
        self.args = args

        # Setup submodules if they exist
        setup_submodules(self.args.path)

        if args.start:
            self.start_app()

        if args.rock_hard_stop:
            self.rock_hard_stop()

    def rock_hard_stop(self):
        """A rock hard stop

        It kills every process in the given directory
        Be it the main process, subprocesses or even zombie processes"""
        py_proces_utils.kill_all_by_cwd_and_subfolders(self.args.path, 15)

    def start_app(self):
        """Starts the app"""
        # Check if the app/repository has submodules and install them
        setup_submodules(self.args.path)

        # If the project uses pipenv, that's the easiest way to install dependencies
        # and run an app.
        if app_runner.check_and_run_pipenv(self.args):
            return
        elif app_runner.run_django_app(self.args):
            return
        elif app_runner.run_simple_app(self.args):
            return

