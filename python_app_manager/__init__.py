import subprocess

from .submodules import process_utils_dev
from . import app_runner


class PythonAppManager:
    def __init__(self, args=None):
        """Python app manager

        :args Parsed arguments given by the command line"""
        self.args = args

        if args.start:
            self.start_app()

        if args.rock_hard_stop:
            self.rock_hard_stop()

    def rock_hard_stop(self):
        """A rock hard stop

        It kills every process in the given directory
        Be it the main process, subprocesses or even zombie processes"""
        process_utils_dev.kill_all_by_cwd_and_subfolders(self.args.path, 15)

    def start_app(self):
        """Starts the app"""
        # If the project uses pipenv, that's the easiest way to install dependencies
        # and run an app.
        if app_runner.check_and_run_pipenv(self.args.path):
            return
