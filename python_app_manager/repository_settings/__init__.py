"""Repository Settings
"""
import os

import psutil


class RepositorySettings:
    repositories: list = []

    def __init__(self, repositories: list):
        # #KeepItDRY
        for repository in repositories:
            name = repository.split(os.path.sep)[-1]

            repository_info = {
                "name": name,
                "path": repository
            }

            self.repositories.append(repository_info)

    def find_by_cwd(self, processes: list, cwd: str):
        """Find a process by cwd on a given list of processes"""
        for proc in processes:
            if proc["cwd"] == cwd:
                return proc
        return None

    def update_repositories_status(self):
        """Update repositories status

        The status is whether a repository is running or not"""
        # Get every running process
        processes = []
        for proc in psutil.process_iter(["pid", "name", "cmdline", "cwd"]):
            pinfo: str = proc.info
            processes.append(pinfo)

        # Show to the user which repositories are running and which aren't
        for repository in self.repositories:
            # Check which repositories are running
            app_status = self.find_by_cwd(processes, repository["path"])

            # Status types:
            # running, restarting, stopped, killed, not_running
            # I don't know if I'm going to implement the other statuses
            if app_status:
                repository["status"] = "running"
            else:
                repository["status"] = "not_running"

    def get_repositories(self):
        """Get repositories"""
        return self.repositories

