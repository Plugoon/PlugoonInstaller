import unreal
import requests
import os

uri = "https://raw.githubusercontent.com/Plugoon/PlugoonInstaller/main/repositories.plugoon"
secretsPath = f"{unreal.Paths.project_plugins_dir()}PlugoonInstaller/Secrets"
secretsFile = f"{secretsPath}/secrets.plugoon"

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
    unreal.log(f"GetPlugoonRepoDetails for {repo}")
    try:
        response = requests.get(uri)
        if response.status_code == 200:
            return response.json()[repo]
        else:
            unreal.log_error("Could not load plugoon repositories")
    except:
        unreal.log_error("Networking error")

def SetPrivateRepoToken(token):
    unreal.log("Set private repo token")
    try:
        file = "secrets.plugoon"
        if not os.path.exists(secretsPath):
            os.makedirs(secretsPath)
        with open(secretsFile, "w") as f:
            f.write(token)
        return True
    except:
        unreal.log_error("Could not save token")
        return False

def GetPrivateRepoToken():
    unreal.log("Get private repo token")
    try:
        with open(secretsFile, "r") as f:
            return f.read()
    except:
        unreal.log_error("Could not load token")
