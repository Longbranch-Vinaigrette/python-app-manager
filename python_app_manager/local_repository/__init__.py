import json
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
        # Python
        python_script_path = f"{self.path}{os.path.sep}main.py"

        # Node.js
        nodejs_script_path = f"{self.path}{os.path.sep}index.js"

        # It's a python app
        if os.path.exists(python_script_path):
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
        elif os.path.exists(nodejs_script_path):
            package_json_path = f"{self.path}{os.path.sep}package.json"

            # Commands
            cmds = "npm install;"

            if os.path.exists(package_json_path):
                # Fetch commands
                with open(package_json_path) as f:
                    try:
                        data = json.load(f)

                        if "scripts" in data:
                            scripts = data['scripts']

                            if "build" in scripts:
                                cmds += f"{scripts['build']};"

                            if "start" in scripts:
                                cmds += f"{scripts['start']};"
                            else:
                                print("Warning: No start script found")
                                # "If start doesn't exist, just start it normally"
                                # - Sigma grindset rule #3492929525235234243245235
                                cmds += f"node index.js"
                        else:
                            print("Warning: Scripts field doesn't exist "
                                  "in package.json")
                            # Start normally
                            cmds += f"node index.js"
                    except:
                        # Start normally
                        print("Warning: Couldn't load data from package.json")
                        cmds += f"node index.js"


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
