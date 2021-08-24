import json
import unreal
import glob
import utils
from typing import Any, List

class Plugin:
    name: str
    version: str
    org: str
    author: str

    def __init__(self, data: Any) -> None:
        self.name = data["FriendlyName"]
        self.version = data["VersionName"]
        self.org = data["Category"]
        self.author = data["CreatedBy"]

def get_installed_plugins() -> List[Plugin]:
    utils.log("Plugin", "get_installed_plugins")
    
    result: List[Plugin] = []
    files = glob.glob(f'{unreal.Paths.project_plugins_dir()}**/*.uplugin', recursive=True)
    for file in files:
        with open(file, "r") as f:
            result.append(Plugin(json.loads(f.read())))
    return result 