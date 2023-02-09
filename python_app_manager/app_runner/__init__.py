import os.path
import subprocess

from ..packages import Packages


def check_and_run_pipenv(args):
    """Check if the app uses pipenv and run the app

    :returns True if it was successful"""
    if os.path.exists(f"{args.path}{os.path.sep}Pipfile"):

        # If the user doesn't have pipenv but the file Pipfile exists
        # in the folder, we can install it.
        pkgs = Packages()
        result = pkgs.find("pipenv")

        if not result:
            # "If the package doesn't exist, just install it" - Sigma grindset rule 420
            subprocess.run(["pip3", "install", "pipenv"])

        # Start the actual app
        subprocess.run(["/bin/bash",
                        "-c",
                        # Cd to the given path
                        f"cd {args.path};"
                        # Normally python projects use main.py to start the app
                        f"pipenv run python3 main.py {args.args};"])
        return True
    else:
        return False


def run_django_app(args):
    """Check if the app is using django and run"""
    # Usually the main script in django apps is 'manage.py'
    script_path = f"{args.path}{os.path.sep}manage.py"
    if os.path.exists(script_path):
        # Start the actual app
        subprocess.run(["/bin/bash",
                        "-c",
                        # Cd to the given path
                        f"cd {args.path};"
                        # Run the app
                        f"python3 manage.py runserver {args.args};"])
        return True
    else:
        return False


def run_simple_app(args):
    """Check if it's a simple app and run"""
    script_path = f"{args.path}{os.path.sep}main.py"
    if os.path.exists(script_path):
        # Start the actual app
        subprocess.run(["/bin/bash",
                        "-c",
                        # Cd to the given path
                        f"cd {args.path};"
                        f"python3 main.py {args.args};"])
        return True
    else:
        return False
