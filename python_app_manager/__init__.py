import subprocess

from .submodules.py_gitconfig import Gitconfig

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
    # Check if these submodules are installed

    for folder in os.listdir(submodule_path):
        is_empty = not os.listdir(f"{submodules_path}{os.path.sep}"
                                  f"{folder}")

        if is_empty:
            # Install submodules and return
            print("There's a submodule missing, installing it...")
            subprocess.run(["/bin/bash",
                            "-c",
                            "git submodule update --remote --init --recursive --merge"])
            return


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
        # It's going to be imported here, in case it doesn't exist.
        from .submodules import process_utils_dev

        process_utils_dev.kill_all_by_cwd_and_subfolders(self.args.path, 15)

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
