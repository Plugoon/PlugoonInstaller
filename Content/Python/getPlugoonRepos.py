import requests
import unreal

unreal.log("get plugoon repositories")
uri = "https://raw.githubusercontent.com/Plugoon/PlugoonInstaller/main/repositories.plugoon"

try:
    response = requests.get(uri)
    if response.status_code == 200:
        unreal.log(response.json())
    else:
        unreal.log_error("Could not load plugoon reposetories")
except:
    unreal.log_error("Networking error")