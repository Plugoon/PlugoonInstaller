import unreal
import requests

class PluginHandle:
    __repoUri = "https://raw.githubusercontent.com/Plugoon/PlugoonInstaller/main/repositories.plugoon"
    
    def __init__(self, handle: str) -> None:
        self.handle = handle
        if not self.__loadHandle():
            raise Exception("Could not create PluginHandle")

    def __loadHandle(self) -> bool:
        try:
            response = requests.get(self.__repoUri)
            if response.status_code == 200:
                for handle in response.json().keys():
                    if self.handle == handle:
                        self.details = response.json()[handle]
                        return True
                unreal.log_warning(f"Handle: {self.handle} doesent exist")
            else:
                unreal.log_warning("Could not load plugoon repositories")
                return False
        except:
            unreal.log_warning("Networking error")
            return False

handle = PluginHandle("blabla")
