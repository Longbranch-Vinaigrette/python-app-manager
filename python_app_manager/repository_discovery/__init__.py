import os


class Discovery:
    repositories: list = []

    def __init__(self):
        self.discover_repositories_recursively()

    def discover_repositories(self, path: str, deepness: int, prepend: str = ""):
        """Get every repository situated at home or one folder below"""
        deepness -= 1

        # Check the depth
        if deepness == 0:
            return

        for name in os.listdir(path):
            current_path = f"{path}{os.path.sep}{name}"
            # print(f"{prepend}\\{name}")

            # Check if it's a folder or not
            if os.path.isdir(current_path):
                # It's a folder
                # Check if it's a repository
                if os.path.exists(f"{current_path}{os.path.sep}.git"):
                    # Add it to the list
                    self.repositories.append(current_path)
                else:
                    # It's not a repository but, we have to look inside it
                    self.discover_repositories(current_path,
                                              deepness,
                                              prepend=f"{prepend}|\t")

    def discover_repositories_recursively(self):
        """Discover repositories recursively"""
        # With three levels of depth, discover repositories
        return self.discover_repositories(os.path.expanduser("~"), 4)

    def get_repositories(self) -> list:
        """Get repositories"""
        return self.repositories
