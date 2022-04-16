import http.client
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