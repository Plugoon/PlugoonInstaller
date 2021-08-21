import unreal
import requests
from version import Version

class Repository:
    _org: str
    _repo: str
    _version: str
    _repo_url: str

    def __init__(self, org: str, repo: str, version: str) -> None:
        self._org = org
        self._repo = repo
        self._version = version
        self._repo_url = f"https://api.github.com/repos/{org}/{repo}/tags"
        if not self._version_check():
            raise Exception("No matching repo found")

    def _version_check(self) -> bool:
        try:
            response = requests.get(self._repo_url)
            if response.status_code != 200:
                unreal.log_warning("could not load repo tags")
                return False
        except:
            unreal.log_warning("Networking error")
            return False
        versions: list[Version] = []
        for entry in response.json():
            try: 
                versions.append(Version(entry["name"]))
            except:
                unreal.log(f"Ignore incompatible version tag {entry['name']} in repo: {self._repo}")
        for v in versions:
            if v.version_unreal == self._version:
                return True    
        return False 

# todo: remove
Repository("Plugoon", "TestRepoPublic", "4.26")
