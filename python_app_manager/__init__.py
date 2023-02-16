import os
import pprint
import subprocess

import psutil

from . import cli_color_messages_python as clr
from .longbranch_vinaigrette_py_repository_discovery.src.repository_discovery \
    import RepositoryDiscovery
from .longbranch_vinaigrette_py_repository_analyzer.src.repositories_processes \
    import RepositoriesProcesses
from .longbranch_vinaigrette_py_repository_configuration \
    import RepositoryConfiguration


class PythonAppManager:
    def __init__(self, path: str):
        """Python app manager"""
        self.path = path

    def setup_all(self):
        """Setup every app"""
        dis = RepositoryDiscovery()
        repositories = dis.get_repositories()

        for rep_abs_path in repositories:
            try:
                clr.print_ok_cyan(f"Updating submodules of {rep_abs_path}")
                rep_config = RepositoryConfiguration(rep_abs_path)
                rep_config.setup_submodules()

                clr.print_ok_green(f"Ok")
            except Exception as ex:
                clr.print_error(f"Error: {str(ex)}")

    def start_app(self):
        """Start the given app"""
        discovered = RepositoryDiscovery()
        rep_procs = RepositoriesProcesses(discovered.get_repositories())
        rep_procs.start_by_cwd(self.path)

    def stop_app(self):
        """Stop the given app"""
        discovered = RepositoryDiscovery()
        rep_procs = RepositoriesProcesses(discovered.get_repositories())
        rep_procs.kill_by_cwd(self.path)
        clr.print_ok_green("App stopped")

    def update_submodules(self):
        """Update app submodules"""
        rep_config = RepositoryConfiguration(self.path)
        rep_config.setup_submodules(force_update=True)
        clr.print_ok_green("App updated")
