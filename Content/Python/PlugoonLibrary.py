import json
from organization import Organization
import unreal
import requests
import os
from plugin_handle import PluginHandle
import plugin
import utils

githubApi = "https://api.github.com"
uri = f"{githubApi}/orgs/Plugoon/repos"
secretsPath = f"{unreal.Paths.project_plugins_dir()}PlugoonInstaller/Secrets"
secretsFile = f"{secretsPath}/secrets.plugoon"

def GetMatchingPlugoonRepos():
    unreal.log("Get plugoon repositries...")
    try:
        response = requests.get(uri)
        if response.status_code == 200:
            result: list[str] = []
            for key in response.json().keys():
                try:
                    result.append(PluginHandle(key).repo_name)
                except:
                    pass
            return result
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
    for plug in plugin.get_installed_plugins():
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

install_plugin("ExamplePlugin")
