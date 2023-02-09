import argparse
import os

from python_app_manager import PythonAppManager

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

# Install submodules automatically just in case
for folder in os.listdir(f"{os.getcwd()}{os.path.sep}"):
    # submodule update --remote --init --recursive --merge
    pass


# Check if the path was given
app_path = args.path
if not app_path:
    raise Exception("No path given, use --path [APP PATH] to give the path "
                    "to an application.")

app_manager = PythonAppManager(args=args)

print("Finished")
