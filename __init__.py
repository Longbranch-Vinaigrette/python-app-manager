import argparse

from src.submodules import process_utils
from src.libs.packages import Packages

parser = argparse.ArgumentParser(description="Python app manager")
parser.add_argument("--path", type=str,
                    help="Application path.")
parser.add_argument("--start", action="store_true",
                    help="Start the application by the given path.")

# Parse args
args = parser.parse_args()

# Check if the path was given
app_path = args.path
if not app_path:
    raise Exception("No path given, use --path [APP PATH] to give the path "
                    "to an application.")

pkgs = Packages()

