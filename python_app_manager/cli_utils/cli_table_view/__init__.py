"""NOT FUNCTIONAL
I Decided to go for the package tabulate, but I want to leave this here to
remember it.
"""


class CLITableView:
    """CLI Table View

    In some interfaces like ps you get output like this:
    root        1463       1  0 13:01 ?        00:00:00 /usr/bin/python3
    root        1664       1  0 13:01 ?        00:00:00 /usr/bin/python3
    felix       3041    2488  0 13:02 ?        00:00:00 /usr/bin/python3

    As you can see the columns are indented, whilst the output of python-app-manager
    looks(currently(2023-02-19)) like this:
    App name			Status		PID		Framework
    perseverancia-backend-api			Running		19951		Unknown
    python-app-manager			Running		19973		Python

    It's not indented, some items have an extra tab and others less tabs.

    So this class is intended to fix that tiny appearance bug.

    Implementation:
    * Check the length of strings to see how many spaces have to be inserted
      between items.
    * Insert spaces between column items.
    * Parse the list into the table view.
    """

    def __init__(self, table: list):
        """CLI Table View

        The table list should be a two-dimensional list containing the rows, example:

        If this is the expected output:
        App name			        Status		PID		Framework
        perseverancia-backend-api	Running		19951	Unknown
        python-app-manager			Running		19973	Python

        Then the given list would look like this:
        [
            ["App name", "Status", "PID", "Framework"],
            ["perseverancia-backend-api", "Running", 19951, "Unknown"],
            ["python-app-manager", "Running", 19973", "Python"],
        ]
        """
        self.table = table
