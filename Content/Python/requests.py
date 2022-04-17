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
        return unreal.PlugoonReposResponse(repos=result)
    if res.status == 401 or res.status == 403:
        return unreal.PlugoonReposResponse(error=unreal.PlugoonError(
            has_error=True,
            message="Invalid access token"
        ))
    return unreal.PlugoonReposResponse(error=unreal.PlugoonError(
        has_error=True,
        message="Unknown error"
    ))

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

def update_repo(name: str, description: str):
    utils.log("update_repo", "started...")
    token = TokenLib.getAccessToken()
    conn = http.client.HTTPSConnection("plugoon.azure-api.net")
    payload = json.dumps({
        'description': description
    })
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    conn.request("PUT", f"/api/repo/{name}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    result = json.loads(data.decode('utf-8'))
    if res.status == 200:
        return unreal.PlugoonRepoResponse(repo=unreal.PlugoonRepo(
            name=result["name"],
            owner=result["owner"],
            description=result["description"],
            packages=result["packages"],
            ue_versions=result["ueVersions"]
        ))
        
    utils.log_error("update_repo", "failed to update Repo")
    if res.status == 401 or res.status == 403:
        return unreal.PlugoonRepoResponse(error=unreal.PlugoonError(
            has_error=True,
            message="Invalid access token"
        ))
    if res.status == 404:
        return unreal.PlugoonRepoResponse(error=unreal.PlugoonError(
            has_error=True,
            message=f"Repo: {name} does not exist"
        ))
    return unreal.PlugoonRepoResponse(error=unreal.PlugoonError(
            has_error=True,
            message=f"Unknown error: {res.status}"
        ))

def delete_repo(name: str):
    utils.log("delete_repo", "started...")
    token = TokenLib.getAccessToken()
    conn = http.client.HTTPSConnection("plugoon.azure-api.net")
    payload = ''
    headers = {
        'Authorization': f'Bearer {token}'
    }
    conn.request("DELETE", f"/api/repo/{name}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    if res.status == 204:
        return unreal.PlugoonError()
    if res.status == 401 or res.status == 403:
        return unreal.PlugoonError(
            has_error=True,
            message="Invalid access token"
        )
    if res.status == 404:
        return unreal.PlugoonError(
            has_error=True,
            message=f"Repo: {name} does not exist"
        )
    return unreal.PlugoonError(
            has_error=True,
            message=f"Unknown error: {res.status}"
        )
