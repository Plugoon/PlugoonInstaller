from __future__ import annotations
import json
import unreal
import glob
import utils

class Plugin:
    name: str
    version: str
    org: str
    author: str

    def __init__(self, data: any) -> None:
        self.name = data["FriendlyName"]
        self.version = data["VersionName"]
        self.org = data["Category"]
        self.author = data["CreatedBy"]

    @classmethod
    def get_installed_plugins(cls) -> list[Plugin]:
        utils.log("Plugin", "get_installed_plugins")
        
        result: list[Plugin] = []
        files = glob.glob(f'{unreal.Paths.project_plugins_dir()}**/*.uplugin', recursive=True)
        for file in files:
            with open(file, "r") as f:
                result.append(cls(json.loads(f.read())))
        return result 