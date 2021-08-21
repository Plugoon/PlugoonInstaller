import unreal
import re

class Version:
    version_unreal: str
    version_plugin: str

    def __init__(self, version: str) -> None:
        match = re.match(r"^ue\d.\d+_v\d+.\d+$", version)
        if not match:
            raise Exception("Invalid tag version")
        self.version_unreal = re.search(r"\d.\d+", match.string).group()
        self.version_plugin = re.search(r"\d+.\d+$", match.string).group()

# todo remove
Version("ue5.0_v1.26")