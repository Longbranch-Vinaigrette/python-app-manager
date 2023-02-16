import pprint
import psutil

from ..longbranch_vinaigrette_py_repository_discovery.src \
    .repository_discovery import RepositoryDiscovery
from .. import cli_color_messages_python as clr
from ..longbranch_vinaigrette_py_repository_analyzer.src.repositories_processes \
    import RepositoriesProcesses
from ..longbranch_vinaigrette_py_repository_configuration \
    import RepositoryConfiguration


class RepositoryManager:
    def __init__(self, args=None):
        # No path has been given, let's start discovering repositories on the
        # user computer.
        dis = RepositoryDiscovery()
        rep_procs = RepositoriesProcesses(dis.get_repositories(), False)

        if args.setup_all:
            dis = RepositoryDiscovery()
            repositories = dis.get_repositories()

            for rep_abs_path in repositories:
                try:
                    clr.print_ok_cyan(f"Updating submodules of {rep_abs_path}")
                    rep_config = RepositoryConfiguration(rep_abs_path)
                    rep_config.setup_submodules()

                    clr.print_ok_green(f"Ok")
                except Exception as ex:
                    clr.print_error(f"Error: {str(ex)}")
        else:
            clr.print_ok_blue("Running repositories/user apps")
            running_apps: dict = rep_procs.get_running_apps()
            print(f"{clr.clr.UNDERLINE}App name{clr.clr.ENDC}\t\t"
                  f"{clr.clr.UNDERLINE}Status{clr.clr.ENDC}\t\t"
                  f"{clr.clr.UNDERLINE}PID{clr.clr.ENDC}")
            for key in list(running_apps.keys()):
                app = running_apps[key]
                print(f"{clr.clr.BOLD}{app['appInfo']['name']}{clr.clr.ENDC}\t"
                      f"{clr.clr.OKGREEN}Running{clr.clr.ENDC}\t\t"
                      f"{clr.clr.WARNING}{app['pid']}{clr.clr.ENDC}")
