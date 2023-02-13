import argparse
import os
import subprocess

import python_app_manager
from python_app_manager import PythonAppManager


def install_submodules():
    # Install submodules automatically just in case
    first_part = "longbranch_vinaigrette_py_"
    # TODO: THIS COULD BE IPMROVED
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
    parser.add_argument("--setup-all", action="store_true",
                        help="Setups every app if possible, it installs/updates submodules "
                        "if they are detected, also installs dependencies if they are "
                        "detected(because I won't add support for everything as there are "
                        "a lot of languages and options).")

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
        from python_app_manager.longbranch_vinaigrette_py_repository_discovery \
            .repository_discovery import Discovery
        from python_app_manager.longbranch_vinaigrette_py_repository_discovery \
            .repository_cli_view import RepositoryCLIView
        from python_app_manager.longbranch_vinaigrette_py_repository_discovery \
            .repository_settings import RepositorySettings

        # No path has been given, let's start discovering repositories on the
        # user computer.
        print("This app will start discovering repositories at the home folder")
        dis = Discovery()
        repository_settings = RepositorySettings(dis.get_repositories())
        repositories_status = RepositoryCLIView(repository_settings)
        repositories_status.show_repositories()
    else:
        # A path to an app has been given, do stuff around
        app_manager = PythonAppManager(args=args)

    print("Finished")
