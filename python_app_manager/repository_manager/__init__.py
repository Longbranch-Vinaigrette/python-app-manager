import pprint
import psutil

from ..longbranch_vinaigrette_py_repository_discovery.src \
    .repository_discovery import Discovery
from ..longbranch_vinaigrette_py_repository_discovery.src \
    .repository_cli_view import RepositoryCLIView
from ..longbranch_vinaigrette_py_repository_discovery.src \
    .repository_settings import RepositorySettings
from ..longbranch_vinaigrette_py_repository_configuration import RepositoryConfiguration
from ..longbranch_vinaigrette_py_repository_analyzer.src.repository_information \
    import RepositoryInformation

from ..longbranch_vinaigrette_py_repository_analyzer.src.repository_information \
    import RepositoryInformation

from .. import cli_color_messages_python as clr

from ..longbranch_vinaigrette_py_repository_analyzer.src.repositories_processes \
    import RepositoriesProcesses


class RepositoryManager:
    def __init__(self, args=None):
        # No path has been given, let's start discovering repositories on the
        # user computer.
        print("This app will start discovering repositories at the home folder")
        dis = Discovery()

        # if args.setup_all:
        #     repositories = dis.get_repositories()
        #
        #     for rep_abs_path in repositories:
        #         try:
        #             clr.print_ok_cyan(f"Updating submodules of {rep_abs_path}")
        #             rep_config = RepositoryConfiguration(rep_abs_path)
        #             rep_config.setup_submodules()
        #
        #             clr.print_ok_green(f"Ok")
        #         except Exception as ex:
        #             clr.print_error(f"Error: {str(ex)}")
        # else:
        #     repositories_status = RepositoryCLIView(repository_settings)
        #     repositories_status.show_repositories()
