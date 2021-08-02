import unreal
import requests

uri = "https://raw.githubusercontent.com/Plugoon/PlugoonInstaller/main/repositories.plugoon"

def GetPlugoonRepo():
    result = []
    result.append()



unreal.log("get plugoon repositories")


try:
    response = requests.get(uri)
    if response.status_code == 200:
        unreal.log(response.json())
    else:
        unreal.log_error("Could not load plugoon reposetories")
except:
    unreal.log_error("Networking error")