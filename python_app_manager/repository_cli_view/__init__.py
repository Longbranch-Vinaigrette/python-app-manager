import os
import psutil


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

    def show_repositories(self):
        """Show every repository running and not running"""
        # Update repositories
        self.update_repositories_status()

        # Print repositories and app statuses
        print(f"\n{clr.UNDERLINE}Repositories{clr.ENDC}")

        # Show to the user which repositories are running and which aren't
        for repository in self.repositories:
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
        self.update_repositories_status()

    def show_only_running_repositories(self):
        """Show only repositories that are running"""
        # Update repositories
        self.update_repositories_status()
