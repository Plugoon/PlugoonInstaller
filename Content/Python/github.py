import unreal
import requests
import utils
from repository import Repository

api = "https://api.github.com"

def get_matching_plugoon_repos():
    return get_matching_repos("Plugoon")

def get_matching_repos(org: str):
    url = f"{api}/orgs/{org}/repos"
    result = dict()
    try:
        response = requests.get(url)
        if response.status_code != 200:
            unreal.log_error(f"Could not load <{org}> repositories")
            return
        for res in response.json():
            if res["name"] == "PlugoonInstaller":
                continue
            try:
                repo = Repository(org, res["name"], utils.get_unreal_version())
                result[repo.name] = {
                    "organization": repo.org,
                    "description": res["description"],
                    "version": "to be implemented",
                    "image": f"https://raw.githubusercontent.com/{org}/{repo.name}/main/Resources/Icon128.png"
                }
            except:
                continue  
        return result
    except:
        unreal.log_error("Networking error")

# todo remove
unreal.log(get_matching_plugoon_repos())