import unreal
import requests
from repository import Repository
import utils


class PluginHandle:
    _repoUri: str = "https://raw.githubusercontent.com/Plugoon/PlugoonInstaller/main/repositories.plugoon"
    repo_name: str
    org: str
    author: str
    repo: Repository
    description: str

    def __init__(self, repo_name: str) -> None:
        self.repo_name = repo_name
        if not self._load_handle():
            raise Exception("Could not create PluginHandle")

    def _load_handle(self) -> bool:
        try:
            response = requests.get(self._repoUri)
            if response.status_code == 200:
                for handle in response.json().keys():
                    if self.repo_name == handle:
                        self.org = response.json()[handle]["Organization"]
                        self.author = response.json()[handle]["Author"]
                        self.description = response.json()[handle]["Description"]
                        try:
                            self.repo = Repository(self.org, self.repo_name, utils.get_unreal_version())
                            return True
                        except:
                            return False
                unreal.log_warning(f"Repository: {self.repo_name} doesent exist for this version")
            else:
                unreal.log_warning("Could not load plugoon repositories")
                return False
        except:
            unreal.log_warning("Networking error")
            return False

# Todo: remove
handle = PluginHandle("TestRepoPublic")
print(handle.author, handle.description, handle.org)
