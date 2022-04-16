import json
from organization import Organization
import unreal
import requests
import os
from plugin_handle import PluginHandle
from plugin import Plugin
import utils

secretsPath = f"{unreal.Paths.project_plugins_dir()}PlugoonInstaller/Secrets"
accessToken = f"{secretsPath}/accessToken.plugoon"
idToken = f"{secretsPath}/idToken.plugoon"


def SetPrivateRepoToken(token: str):
    unreal.log("Set private repo token")
    try:
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

def install_plugin(handle: str) -> bool:
    repo: str = ''
    try:
        repo = Organization("Plugoon").get_matching_repos()["data"][handle]
    except:
        utils.log_error("install_plugin", f"plugin {handle} doesent exist")
        return False
    for plug in Plugin.get_installed_plugins():
        if handle == plug.name:
            unreal.log_warning(f"Plugin {handle} is allready installed")

def GetUnrealVersion():
    unreal.log("GetUnrealVersion")
    with open(unreal.Paths.get_project_file_path(), "r") as f:
        result = json.loads(f.read())
        return result["EngineAssociation"]

def GetRepoTags(org: str, repo: str):
    unreal.log(f"GetRepoTags for org: {org}, repo: {repo}")
    try:
        repoUrl = f"{githubApi}/repos/{org}/{repo}"
        url = f"{repoUrl}/tags"
        response = requests.get(url)
        if response.status_code == 200:
            unreal.log(response.json())
        else:
            unreal.log_error("Could not load plugoon repositories")
    except:
        unreal.log_error("Networking error")
    return "nothing"

