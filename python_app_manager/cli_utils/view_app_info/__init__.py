from tabulate import tabulate


class ViewAppInfo:
    """View App Info

    Views app info like a table:
    App name			        Status		PID		Framework
    perseverancia-backend-api	Running		19951	Unknown
    python-app-manager			Running		22676	Python

    Implementation:
    * Receive app data from repository_analyzer submodule and parse
      it to data for a table view
    * Show the data like a table
    """

    def __init__(self):
        """Parse App Info"""
        pass