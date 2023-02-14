import pprint

from ..longbranch_vinaigrette_py_repository_discovery \
    .repository_discovery import Discovery
from ..longbranch_vinaigrette_py_repository_discovery \
    .repository_cli_view import RepositoryCLIView
from ..longbranch_vinaigrette_py_repository_discovery \
    .repository_settings import RepositorySettings
from ..longbranch_vinaigrette_py_repository_configuration import RepositoryConfiguration


class RepositoryManager:
    def __init__(self, args=None):
        # No path has been given, let's start discovering repositories on the
        # user computer.
        print("This app will start discovering repositories at the home folder")
        dis = Discovery()
        repository_settings = RepositorySettings(dis.get_repositories())
        repositories_status = RepositoryCLIView(repository_settings)

        if args.setup_all:
            repositories = dis.get_repositories()
            pprint.pprint(repositories)

            for rep_abs_path in repositories:
                print("Absolute path: ", rep_abs_path)
                rep_config = RepositoryConfiguration(rep_abs_path)
                rep_config.setup_submodules()
        else:
            repositories_status.show_repositories()

