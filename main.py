import argparse
import os
import subprocess


def install_submodules():
    """Hmmm, I think I'm not gonna use this chunk of code"""
    # Install submodules automatically just in case
    first_part = "longbranch_vinaigrette_py_"
    submodules_name = [
        f"longbranch_vinaigrette_py_desktop_entry",
        f"longbranch_vinaigrette_py_gitconfig",
        f"longbranch_vinaigrette_py_process_utils",
        f"longbranch_vinaigrette_py_repository_configuration",
        f"longbranch_vinaigrette_py_repository_discovery"
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
    from python_app_manager import PythonAppManager

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

    # install_submodules()

    # Check if the path was given
    app_path = args.path
    if not app_path:
        from python_app_manager.repository_manager import RepositoryManager
        RepositoryManager(args=args)
    else:
        # A path to an app has been given, do stuff around
        app_manager = PythonAppManager(args=args)
