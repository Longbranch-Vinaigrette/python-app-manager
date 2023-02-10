import os
import pprint
import subprocess

import psutil

from .local_repository import LocalRepository


class PythonAppManager(LocalRepository):
    def __init__(self, args=None):
        """Python app manager

        :args Parsed arguments given by the command line"""
        super().__init__(args.path)
        self.args = args

        # Setup submodules if they exist
        setup_submodules(self.args.path)

        if args.start:
            self.start_app()

        if args.rock_hard_stop:
            self.rock_hard_stop()

