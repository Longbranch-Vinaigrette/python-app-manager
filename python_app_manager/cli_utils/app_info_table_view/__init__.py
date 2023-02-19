import pprint

from tabulate import tabulate

from ... import cli_color_messages_python as clr


class AppInfoTableView:
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

    def __init__(self,
                 # The app info
                 app_info: dict,
                 # What fields to view when the table is printed on the console
                 view_columns: list =
                    [
                        "appInfo:name",
                        "status",
                        "pid",
                        "appInfo:appLanguage",
                        "appInfo:framework"
                    ]
                 ):
        """App info table view

        app_info The app info given by repository_analyzer submodule
        view_columns A list of the columns the user wants to see.
            In the app info given by repository_analyzer there's also a sub dictionary
            with the field name 'appInfo' which has information fetched from the
            app itself.
            To reference this use appInfo:[Field]"""
        self.table = self.parse_app_info(app_info, view_columns)
        headers = self.get_headers(view_columns)
        print(tabulate(self.table, headers=headers))

    def get_headers(self, view_columns):
        """Get headers"""
        view_app_name = "appInfo:name" in view_columns
        view_status = "status" in view_columns
        view_pid = "pid" in view_columns
        view_language = "appInfo:appLanguage" in view_columns
        view_framework = f"appInfo:framework" in view_columns

        headers: list = []

        def get_underlined(txt: str):
            """Convert text to underline"""
            return f"{clr.clr.UNDERLINE}{txt}{clr.clr.ENDC}"

        if view_app_name:
            headers.append(get_underlined("App name"))
        if view_status:
            headers.append(get_underlined("Status"))
        if view_pid:
            headers.append(get_underlined("PID"))
        if view_language:
            headers.append(get_underlined("Language"))
        if view_framework:
            headers.append(get_underlined("Framework"))

        return headers

    def parse_app_info(self, app_info: dict, view_columns: list):
        """Parse app info"""
        result: list = []
        view_app_name = "appInfo:name" in view_columns
        view_status = "status" in view_columns
        view_pid = "pid" in view_columns
        view_language = "appInfo:appLanguage" in view_columns
        view_framework = f"appInfo:framework" in view_columns

        for key in list(app_info.keys()):
            item = app_info[key]
            appInfo = item["appInfo"]
            row: list = []

            # View the app name
            if view_app_name:
                row.append(
                    f"{clr.clr.BOLD}"
                    f"{appInfo['name']}"
                    f"{clr.clr.ENDC}"
                )

            # View the status
            if view_status:
                # If the dictionary has the field pid and it's not None
                # then it's running
                if "pid" in item and item["pid"] is not None:
                    row.append(f"{clr.clr.OKGREEN}"
                               f"Running"
                               f"{clr.clr.ENDC}")
                else:
                    row.append(f"{clr.clr.FAIL}"
                               f"Not running"
                               f"{clr.clr.ENDC}")

            # View the pid
            if view_pid:
                if "pid" in item and item["pid"] is not None:
                    row.append(f"{clr.clr.OKCYAN}"
                               f"{item['pid']}"
                               f"{clr.clr.ENDC}")
                else:
                    row.append(f"{clr.clr.FAIL}"
                               f"Not running"
                               f"{clr.clr.ENDC}")

            # View app language
            if view_language:
                row.append(appInfo["appLanguage"])

            # View framework
            if view_framework:
                # Check if the app framework was detected or not
                if appInfo["framework"] == "Unknown":
                    app_framework_info = f"{clr.clr.WARNING}" \
                                         f"{appInfo['framework']}" \
                                         f"{clr.clr.ENDC}"
                elif appInfo["framework"]:
                    app_framework_info = f"{clr.clr.OKGREEN}" \
                                         f"{appInfo['framework']}" \
                                         f"{clr.clr.ENDC}"
                else:
                    app_framework_info = f"{clr.clr.FAIL}" \
                                         f"Error" \
                                         f"{clr.clr.ENDC}"
                row.append(app_framework_info)

            # Append row
            result.append(row)

        return result
