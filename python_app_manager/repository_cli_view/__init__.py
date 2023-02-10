import os
import psutil

from ..repository_settings import RepositorySettings


# Console colors
class clr:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class RepositoryCLIView:
    repositories: list = []

    def __init__(self, repository_settings: RepositorySettings):
        self.repository_settings = repository_settings

    def show_repositories(self):
        """Show every repository running and not running"""
        # Update repositories
        self.repository_settings.update_repositories_status()

        # Print repositories and app statuses
        print(f"\n{clr.UNDERLINE}Repositories{clr.ENDC}")

        # Show to the user which repositories are running and which aren't
        for repository in self.repository_settings.get_repositories():
            print(f"- {repository['name']}")
            print(f"\tIts path: {repository['path']}")

            app_status = repository["status"]

            # Status types:
            # running, restarting, stopped, killed, not_running
            if app_status == "running":
                print(f"\t{clr.OKGREEN}Status: Running{clr.ENDC}")
            elif app_status == "not_running":
                print(f"\t{clr.FAIL}Status: Not running{clr.ENDC}")
            elif app_status == "restarting":
                print(f"\t{clr.OKBLUE}Status: Restarting{clr.ENDC}")
            elif app_status == "stopped":
                print(f"\t{clr.WARNING}Status: Stopped{clr.ENDC}")
            elif app_status == "killed":
                print(f"\t{clr.FAIL}Status: Killed{clr.ENDC}")
            else:
                print(f"\t{clr.FAIL}Status: Unknown status{clr.ENDC}")

    def print_repositories_as_json(self):
        """For output capturing"""
        # Update repositories
        self.repository_settings.update_repositories_status()

    def show_only_running_repositories(self):
        """Show only repositories that are running"""
        # Update repositories
        self.repository_settings.update_repositories_status()
