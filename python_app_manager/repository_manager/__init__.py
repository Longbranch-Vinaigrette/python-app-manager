import pprint
import psutil

from ..longbranch_vinaigrette_py_repository_discovery.src \
    .repository_discovery import RepositoryDiscovery
from .. import cli_color_messages_python as clr
from ..longbranch_vinaigrette_py_repository_analyzer.src.repositories_processes \
    import RepositoriesProcesses
from ..longbranch_vinaigrette_py_repository_configuration \
    import RepositoryConfiguration

from ..cli_utils.app_info_table_view import AppInfoTableView


class RepositoryManager:
    def __init__(self, args=None):
        # No path has been given, let's start discovering repositories on the
        # user computer.
        dis = RepositoryDiscovery()
        rep_procs = RepositoriesProcesses(dis.get_repositories(), debug=False)

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
        elif args.show_all:
            clr.print_ok_blue("Apps found")
            apps: dict = rep_procs.get_apps()
            table_view = AppInfoTableView(
                apps,
                # view_columns=[
                #         "appInfo:name",
                #         "appInfo:appLanguage",
                #         "appInfo:framework"
                #     ]
            )
        else:
            clr.print_ok_blue("Running repositories/user apps")

            # Get running apps(it's a dictionary in which the keys
            # are the path to the app/repository)
            running_apps: dict = rep_procs.get_running_apps()

            # Print the apps state as a table
            table_view = AppInfoTableView(running_apps)
