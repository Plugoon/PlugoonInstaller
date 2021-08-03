import unreal
import requests

uri = "https://raw.githubusercontent.com/Plugoon/PlugoonInstaller/main/repositories.plugoon"

def GetPlugoonRepo():
    unreal.log("Get plugoon repositries...")
    try:
        response = requests.get(uri)
        if response.status_code == 200:
            return response.json().keys()
        else:
            unreal.log_error("Could not load plugoon repositories")
    except:
        unreal.log_error("Networking error")

def GetPlugoonRepoDetails(repo):
    unreal.log(F"GetPlugoonRepoDetails for {repo}")
    try:
        response = requests.get(uri)
        if response.status_code == 200:
            # return response.json()[repo]
            return {
                "data": "value",
                "version": "1.0.0"
                }
        else:
            unreal.log_error("Could not load plugoon repositories")
    except:
        unreal.log_error("Networking error")