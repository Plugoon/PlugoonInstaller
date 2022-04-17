import http.client
from os import stat
import TokenLib
import utils
import json
import unreal

def get_repos():
    utils.log("get_repos", "started...")
    token = TokenLib.getAccessToken()
    conn = http.client.HTTPSConnection("plugoon.azure-api.net")
    payload = ''
    headers = {
        'Authorization': f'Bearer {token}'
    }
    conn.request("GET", "/api/repo", payload, headers)
    res = conn.getresponse()
    data = res.read()
    if res.status == 200:
        repos = json.loads(data.decode("utf-8"))
        result = []
        for repo in repos:
            result.append(unreal.PlugoonRepo(
                name=repo["name"],
                owner=repo["owner"],
                description=repo["description"],
                ue_versions=repo["ueVersions"],
                packages=repo["packages"]
            ))
        return result
    else:
        utils.log_error("get_repos", "repos not found")
        return []

def add_repo(name: str, description: str):
    utils.log("add_repos", "started...")
    token = TokenLib.getAccessToken()
    conn = http.client.HTTPSConnection("plugoon.azure-api.net")
    payload = json.dumps({
        'name': name,
        'description': description
    })
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/api/repo", payload, headers)
    res = conn.getresponse()
    data = res.read()
    repo = json.loads(data.decode('utf-8'))
    if res.status == 201:
        return unreal.PlugoonRepoResponse(repo=unreal.PlugoonRepo(
            name=repo["name"],
            owner=repo["owner"],
            description=repo["description"],
            packages=repo["packages"],
            ue_versions=repo["ueVersions"]
        ))
        
    utils.log_error("add_repo", "failed to add Repo")
    if res.status == 401 or res.status == 403:
        return unreal.PlugoonRepoResponse(error=unreal.PlugoonError(
            has_error=True,
            message="Invalid access token"
        ))
    if res.status == 409:
        return unreal.PlugoonRepoResponse(error=unreal.PlugoonError(
            has_error=True,
            message=f"Repo: {name} allready exist"
        ))
    return unreal.PlugoonRepoResponse(error=unreal.PlugoonError(
            has_error=True,
            message=f"Unknown error: {res.status}"
        ))