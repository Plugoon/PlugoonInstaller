import unreal
import requests


class PluginHandle:
    _repoUri: str = "https://raw.githubusercontent.com/Plugoon/PlugoonInstaller/main/repositories.plugoon"
    handle: str
    org: str
    author: str
    description: str

    def __init__(self, handle: str) -> None:
        self.handle = handle
        if not self._load_handle():
            raise Exception("Could not create PluginHandle")

    def _load_handle(self) -> bool:
        try:
            response = requests.get(self._repoUri)
            if response.status_code == 200:
                for handle in response.json().keys():
                    if self.handle == handle:
                        self.org = response.json()[handle]["Organization"]
                        self.author = response.json()[handle]["Author"]
                        self.description = response.json()[
                            handle]["Description"]
                        return True
                unreal.log_warning(f"Handle: {self.handle} doesent exist")
            else:
                unreal.log_warning("Could not load plugoon repositories")
                return False
        except:
            unreal.log_warning("Networking error")
            return False

# Todo: remove
handle = PluginHandle("ExampleRepo")
print(handle.author, handle.description, handle.org)
