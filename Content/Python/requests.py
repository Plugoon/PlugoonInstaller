import http.client
import TokenLib
import utils
import json
import unreal

def get_repos(version: str):
    utils.log("get_repos", "started...")
    token = TokenLib.getAccessToken()
    conn = http.client.HTTPSConnection("plugoon.azure-api.net")
    payload = ''
    headers = {
        'Authorization': f'Bearer {token}'
    }
    conn.request("GET", f"/api/repo?version={version}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    conn.close()
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

def get_owned_repos():
    utils.log("get_owned_repos", "started...")
    token = TokenLib.getAccessToken()
    conn = http.client.HTTPSConnection("plugoon.azure-api.net")
    payload = ''
    headers = {
        'Authorization': f'Bearer {token}'
    }
    conn.request("GET", f"/api/repo?owner=true", payload, headers)
    res = conn.getresponse()
    data = res.read()
    conn.close()
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
    conn.close()
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
    conn.close()
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
    conn.close()
    if res.status == 204:
        return unreal.PlugoonError()
    utils.log_error("delete_repo", "failed to update Repo")
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
    if res.status == 409:
        return unreal.PlugoonError(
            has_error=True,
            message=f"Repo: {name} still has packages -> delete packages first"
        )
    return unreal.PlugoonError(
            has_error=True,
            message=f"Unknown error: {res.status}"
        )

def get_packages(name: str):
    utils.log("get_packages", "started...")
    token = TokenLib.getAccessToken()
    conn = http.client.HTTPSConnection("plugoon.azure-api.net")
    payload = ''
    headers = {
        'Authorization': f'Bearer {token}'
    }
    conn.request("GET", f"/api/repo/{name}/package", payload, headers)
    res = conn.getresponse()
    data = res.read()
    conn.close()
    if res.status == 200:
        packages = json.loads(data.decode("utf-8"))
        result = []
        for package in packages:
            result.append(unreal.PlugoonPackage(
                id=package["id"],
                repo_name=package["repoName"],
                package_version=package["packageVersion"],
                ue_version=package["ueVersion"],
                deprecated=package["deprecated"],
                url=package["url"],
                dependencies=package["dependencies"]
            ))
        return unreal.PlugoonPackagesResponse(packages=result)
    if res.status == 401 or res.status == 403:
        return unreal.PlugoonPackagesResponse(error=unreal.PlugoonError(
            has_error=True,
            message="Invalid access token"
        ))
    if res.status == 404:
        return unreal.PlugoonPackagesResponse(error=unreal.PlugoonError(
            has_error=True,
            message=f"Repo: {name} not found"
        ))
    return unreal.PlugoonPackagesResponse(error=unreal.PlugoonError(
        has_error=True,
        message="Unknown error"
    ))

def add_package(name: str, ue_version: str, package_version: str, url: str, dependencies):
    utils.log("add_package", "started...")
    token = TokenLib.getAccessToken()
    conn = http.client.HTTPSConnection("plugoon.azure-api.net")
    depList = []
    for dep in dependencies:
        depList.append(dep)
    payload = json.dumps({
        "ueVersion": ue_version,
        "packageVersion": package_version,
        "url": url,
        "dependencies": depList
    })
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    conn.request("POST", f"/api/repo/{name}/package", payload, headers)
    res = conn.getresponse()
    data = res.read()
    conn.close()
    if res.status == 201:
        package = json.loads(data.decode("utf-8"))
        return unreal.PlugoonPackageResponse(package=unreal.PlugoonPackage(
            id=package["id"],
            repo_name=package["repoName"],
            package_version=package["packageVersion"],
            ue_version=package["ueVersion"],
            deprecated=package["deprecated"],
            url=package["url"],
            dependencies=package["dependencies"]
        ))
    if res.status == 401 or res.status == 403:
        return unreal.PlugoonPackageResponse(error=unreal.PlugoonError(
            has_error=True,
            message="Invalid access token"
        ))
    if res.status == 404:
        return unreal.PlugoonPackageResponse(error=unreal.PlugoonError(
            has_error=True,
            message=f"Repo: {name} not found"
        ))
    if res.status == 409:
        return unreal.PlugoonPackageResponse(error=unreal.PlugoonError(
            has_error=True,
            message=f"Package with keys repo: {name}, unrealVersion: {ue_version}," + 
                f"packageVersion: {package_version} allready exists"
        ))
    return unreal.PlugoonPackageResponse(error=unreal.PlugoonError(
        has_error=True,
        message="Unknown error"
    ))

def get_package(name: str, packageId: str):
    utils.log("get_package", "started...")
    token = TokenLib.getAccessToken()
    conn = http.client.HTTPSConnection("plugoon.azure-api.net")
    payload = ''
    headers = {
        'Authorization': f'Bearer {token}',
    }
    conn.request("GET", f"/api/repo/{name}/package/{packageId}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    conn.close()
    if res.status == 200:
        package = json.loads(data.decode("utf-8"))
        return unreal.PlugoonPackageResponse(package=unreal.PlugoonPackage(
            id=package["id"],
            repo_name=package["repoName"],
            package_version=package["packageVersion"],
            ue_version=package["ueVersion"],
            deprecated=package["deprecated"],
            url=package["url"],
            dependencies=package["dependencies"]
        ))
    if res.status == 401 or res.status == 403:
        return unreal.PlugoonPackageResponse(error=unreal.PlugoonError(
            has_error=True,
            message="Invalid access token"
        ))
    if res.status == 404:
        return unreal.PlugoonPackageResponse(error=unreal.PlugoonError(
            has_error=True,
            message=f"Package: {packageId} not found on repo: {name}"
        ))
    return unreal.PlugoonPackageResponse(error=unreal.PlugoonError(
        has_error=True,
        message=f"Unknown error: {res.status}"
    ))

def update_package(name: str, packageId: str, url: str):
    utils.log("update_package", "started...")
    token = TokenLib.getAccessToken()
    conn = http.client.HTTPSConnection("plugoon.azure-api.net")
    payload = json.dumps({
        "url": url
    })
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    conn.request("PUT", f"/api/repo/{name}/package/{packageId}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    conn.close()
    if res.status == 200:
        package = json.loads(data.decode("utf-8"))
        return unreal.PlugoonPackageResponse(package=unreal.PlugoonPackage(
            id=package["id"],
            repo_name=package["repoName"],
            package_version=package["packageVersion"],
            ue_version=package["ueVersion"],
            deprecated=package["deprecated"],
            url=package["url"],
            dependencies=package["dependencies"]
        ))
    if res.status == 401 or res.status == 403:
        return unreal.PlugoonPackageResponse(error=unreal.PlugoonError(
            has_error=True,
            message="Invalid access token"
        ))
    if res.status == 404:
        return unreal.PlugoonPackageResponse(error=unreal.PlugoonError(
            has_error=True,
            message=f"Package: {packageId} not found on repo: {name}"
        ))
    return unreal.PlugoonPackageResponse(error=unreal.PlugoonError(
        has_error=True,
        message=f"Unknown error: {res.status}"
    ))

def deprecate_package(name: str, packageId: str):
    utils.log("deprecate_package", "started...")
    token = TokenLib.getAccessToken()
    conn = http.client.HTTPSConnection("plugoon.azure-api.net")
    payload = json.dumps({
        "deprecated": True
    })
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    conn.request("PUT", f"/api/repo/{name}/package/{packageId}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    conn.close()
    if res.status == 200:
        package = json.loads(data.decode("utf-8"))
        return unreal.PlugoonPackageResponse(package=unreal.PlugoonPackage(
            id=package["id"],
            repo_name=package["repoName"],
            package_version=package["packageVersion"],
            ue_version=package["ueVersion"],
            deprecated=package["deprecated"],
            url=package["url"],
            dependencies=package["dependencies"]
        ))
    if res.status == 401 or res.status == 403:
        return unreal.PlugoonPackageResponse(error=unreal.PlugoonError(
            has_error=True,
            message="Invalid access token"
        ))
    if res.status == 404:
        return unreal.PlugoonPackageResponse(error=unreal.PlugoonError(
            has_error=True,
            message=f"Package: {packageId} not found on repo: {name}"
        ))
    return unreal.PlugoonPackageResponse(error=unreal.PlugoonError(
        has_error=True,
        message=f"Unknown error: {res.status}"
    ))

def delete_package(name: str, packageId: str):
    utils.log("delete_package", "started...")
    token = TokenLib.getAccessToken()
    conn = http.client.HTTPSConnection("plugoon.azure-api.net")
    payload = ''
    headers = {
        'Authorization': f'Bearer {token}'
    }
    conn.request("DELETE", f"/api/repo/{name}/package/{packageId}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    conn.close()
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
            message=f"Package: {packageId} not found on repo: {name}"
        )
    return unreal.PlugoonError(
        has_error=True,
        message=f"Unknown error: {res.status}"
    )

def get_install_list(name: str, packageId: str):
    utils.log("get_install_list", "started...")
    token = TokenLib.getAccessToken()
    conn = http.client.HTTPSConnection("plugoon.azure-api.net")
    payload = ''
    headers = {
        'Authorization': f'Bearer {token}'
    }
    conn.request("GET", f"/api/repo/{name}/package/{packageId}/install", payload, headers)
    res = conn.getresponse()
    data = res.read()
    conn.close()
    if res.status == 200:
        packages = json.loads(data.decode("utf-8"))
        result = []
        for package in packages:
            result.append(unreal.PlugoonPackage(
                id=package["id"],
                repo_name=package["repoName"],
                package_version=package["packageVersion"],
                ue_version=package["ueVersion"],
                deprecated=package["deprecated"],
                url=package["url"],
                dependencies=package["dependencies"]
            ))
        return unreal.PlugoonPackagesResponse(packages=result)
    if res.status == 401 or res.status == 403:
        return unreal.PlugoonPackagesResponse(error=unreal.PlugoonError(
            has_error=True,
            message="Invalid access token"
        ))
    if res.status == 404:
        return unreal.PlugoonPackagesResponse(error=unreal.PlugoonError(
            has_error=True,
            message=f"Package: {packageId} not found on repo {name}"
        ))
    return unreal.PlugoonPackagesResponse(error=unreal.PlugoonError(
        has_error=True,
        message="Unknown error"
    ))
