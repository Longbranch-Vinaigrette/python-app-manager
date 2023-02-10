import os

from ..longbranch_vinaigrette_py_gitconfig import Gitconfig
from ..longbranch_vinaigrette_py_desktop_entry import DesktopEntry
from .. import longbranch_vinaigrette_py_process_utils as process_utils
from ..repository_cli_view import print_error


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


class LocalRepository:
    def __init__(self, path: str, args: str = ""):
        self.path = path
        self.args = args

    def get_repository_name(self):
        return self.path.split(os.path.sep)[-1]

    def rock_hard_stop(self):
        """A rock hard stop

        It kills every process in the given directory
        Be it the main process, subprocesses or even zombie processes"""
        process_utils.kill_all_by_cwd_and_subfolders(self.path, 15)

    def get_app_run_command(self):
        """Get app run command"""
        script_path = f"{args.path}{os.path.sep}main.py"

        if os.path.exists(script_path):
            # Check if it uses pipenv
            if os.path.exists(f"{self.path}{os.path.sep}Pipfile"):
                # If the user doesn't have pipenv but the file Pipfile exists
                # in the folder, we can install it.
                pkgs = Packages()
                result = pkgs.find("pipenv")

                if not result:
                    # "If the package doesn't exist, just install it" - Sigma grindset rule 420
                    subprocess.run(["pip3", "install", "pipenv"])

                return f"pipenv run python3 main.py {self.args};"
            else:
                # Normal python app
                return f"python3 main.py {self.args};"

    def start_app(self):
        """Starts the app"""
        # Check if the app/repository has submodules and install them
        setup_submodules(self.path)

        # Get app run command
        run_cmd = self.get_app_run_command()
        if run_cmd:
            # Run app
            return subprocess.run(["/bin/bash",
                                   "-c",
                                   f"cd {self.path};"
                                   f"{run_cmd}"])
        # Error
        return print_error("Couldn't find a way to run the app.")

    def toggle_start_on_boot(self):
        """Toggle start on boot"""
        desktop_entry = DesktopEntry(self.path,
                                     self.get_repository_name(),
                                     self.get_app_run_command())
        desktop_entry.toggle_start_on_boot()
