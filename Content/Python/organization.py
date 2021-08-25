from datetime import datetime
import os
import unreal
import requests
import utils
from repository import Repository
import json

class Organization:
    _api: str
    org: str
    _temp_path: str = f"{unreal.Paths.project_plugins_dir()}PlugoonInstaller/Temp"

    def __init__(self, org: str) -> None:
        self.org = org
        self._api = f"https://api.github.com/orgs/{org}"

    def get_matching_repos(self):
        utils.log("Organization", "get_matching_repos")
        url = f"{self._api}/repos"
        storedData = self._load()
        if storedData:
            if datetime.now().timestamp() - storedData['timestamp'] < 180:
                return storedData
        result = dict()
        try:
            response = requests.get(url)
            if response.status_code != 200:
                if response.status_code == 403:
                    utils.log_warning("get_matching_repos", "Reached max numbers of requests")
                utils.log_warning("get_matching_repos", f"Could not load <{self.org}> repositories")
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
            result = {
                "timestamp": datetime.now().timestamp(),
                "data": result
            }
            self._save(result)
            return result
        except:
            utils.log_warning("get_matching_repos", "Networking error")
            if storedData:
                utils.log_warning("get_matching_repos", "return local stored data")
                return storedData
            utils.log_error("get_matching_repos", "could not find data")
            

    def _save(self, data) -> None:
        utils.log("Organization", "_save")
        json_string = json.dumps(data, indent=4, separators=(',', ': '))
        try:
            if not os.path.exists(self._temp_path):
                os.makedirs(self._temp_path)
            with open(f"{self._temp_path}/organization.json", "w") as f:
                f.write(json_string)
        except:
            utils.log_error("_save", "could not write to organization.json")

    def _load(self):
        utils.log("organization", "_load")
        if not os.path.exists(f"{self._temp_path}/organization.json"):
            return None
        try:
            with open(f"{self._temp_path}/organization.json", "r") as f:
                return json.loads(f.read())
        except:
            utils.log_error("_load", "could not read from organization.json")
