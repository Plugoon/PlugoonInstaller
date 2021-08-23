from datetime import datetime
import unreal
import requests
import utils
from repository import Repository

class Organization:
    _api: str
    org: str

    def __init__(self, org: str) -> None:
        self.org = org
        self._api = f"https://api.github.com/orgs/{org}"

    def get_matching_repos(self):
        url = f"{self._api}/repos"
        result = dict()
        try:
            response = requests.get(url)
            if response.status_code != 200:
                if response.status_code == 403:
                    unreal.log_warning("Reached max numbers of requests")
                unreal.log_warning(f"Could not load <{self.org}> repositories")
            for res in response.json():
                if res["name"] == "PlugoonInstaller":
                    continue
                try:
                    repo = Repository(self.org, res["name"], utils.get_unreal_version())
                    result[repo.name] = {
                        "organization": repo.org,
                        "description": res["description"],
                        "version": "0.0",
                        "image": f"https://raw.githubusercontent.com/{self.org}/{repo.name}/main/Resources/Icon128.png"
                    }
                except:
                    continue
            return {
                "timestamp": datetime.now(),
                "data": result
            }
        except:
            unreal.log_error("Networking error")
