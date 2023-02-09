import argparse
import os
import subprocess

from python_app_manager import PythonAppManager


def install_submodules():
    # Install submodules automatically just in case
    submodules_path = f"{os.getcwd()}{os.path.sep}" \
                     f"python_app_manager{os.path.sep}" \
                     f"submodules"
    for folder in os.listdir(submodules_path):
        # submodule update --remote --init --recursive --merge
        is_empty = not os.listdir(f"{submodules_path}{os.path.sep}"
                                  f"{folder}")

        if is_empty:
            # Install submodules and return
            print("There's a submodule missing, installing it...")
            subprocess.run(["/bin/bash",
                            "-c",
                            "git submodule update --remote --init --recursive --merge"])
            return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python app manager")

    # App path(required)
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

    # Parse args
    args = parser.parse_args()

    install_submodules()

    # Check if the path was given
    app_path = args.path
    if not app_path:
        raise Exception("No path given, use --path [APP PATH] to give the path "
                        "to an application.")

    app_manager = PythonAppManager(args=args)

    print("Finished")
