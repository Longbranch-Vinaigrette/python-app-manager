import argparse
import os
import subprocess

import python_app_manager
from python_app_manager import PythonAppManager
from python_app_manager.repository_discovery import Discovery
from python_app_manager.repository_cli_view import RepositoryCLIView


def install_submodules():
    # Install submodules automatically just in case
    first_part = "longbranch_vinaigrette_py_"
    submodules_name = [
        f"{first_part}desktop_entry",
        f"{first_part}gitconfig",
        f"{first_part}process_utils"
    ]
    for name in submodules_name:
        is_empty = not os.listdir(f"{os.getcwd()}{os.path.sep}"
                                  f"python_app_manager{os.path.sep}"
                                  f"{name}")

        if is_empty:
            # Install submodules and return
            print("There's a submodule missing, installing every submodule in "
                  "existence...")
            subprocess.run(["/bin/bash",
                            "-c",
                            "git submodule update --remote --init --recursive --merge"])
            return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python app manager")

    # App path(for single app setup)
    parser.add_argument("--path", type=str,
                        help="Application path.")

    # Actions
    parser.add_argument("--start", action="store_true",
                        help="Start the application by the given path.")
    parser.add_argument("--stop", action="store_true",
                        help="Stops an application by the given path.")

    # Other options
    parser.add_argument("--rock-hard-stop", action="store_true",
                        help="Stops the application on the given path by"
                             "using brute force.")
    parser.add_argument("--args", type=str,
                        help="Application arguments.")

    # Parse args
    args = parser.parse_args()

    install_submodules()

    # Check if the path was given
    app_path = args.path
    if not app_path:
        # No path has been given, let's start discovering repositories on the
        # user computer.
        print("This app will start discovering repositories at the home folder")
        dis = Discovery()
        repositories_status = RepositoryCLIView(dis.get_repositories())
        repositories_status.show_repositories()
    else:
        # A path to an app has been given, do stuff around
        app_manager = PythonAppManager(args=args)

    print("Finished")
