import os
import pprint
import subprocess

import psutil

from .longbranch_vinaigrette_py_repository_discovery.src.repository_discovery \
    import RepositoryDiscovery


class PythonAppManager:
    def __init__(self, path: str):
        """Python app manager"""
        self.path = path

    def start_app(self):
        """Start the given app"""
        pass

    def stop_app(self):
        """Stop the given app"""

