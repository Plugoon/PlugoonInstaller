import unreal
import os

secretsPath = f"{unreal.Paths.project_plugins_dir()}PlugoonInstaller/Secrets"
accessToken = f"{secretsPath}/accessToken.plugoon"
idToken = f"{secretsPath}/idToken.plugoon"

def setIdToken(token: str):
    unreal.log("Set id token")
    try:
        if not os.path.exists(secretsPath):
            os.makedirs(secretsPath)
        with open(idToken, "w") as f:
            f.write(token)
        return True
    except:
        unreal.log_error("Could not save token")
        return False

def setAccessToken(token: str):
    unreal.log("Set access token")
    try:
        if not os.path.exists(secretsPath):
            os.makedirs(secretsPath)
        with open(accessToken, "w") as f:
            f.write(token)
        return True
    except:
        unreal.log_error("Could not save token")
        return False

def getIdToken() -> str:
    unreal.log("Get id token")
    try:
        with open(idToken, "r") as f:
            return f.read()
    except:
        unreal.log_error("Could not load id token")

def getAccessToken() -> str:
    unreal.log("Get access token")
    try:
        with open(accessToken, "r") as f:
            return f.read()
    except:
        unreal.log_error("Could not load access token")

def getTokens():
    accessToken = getAccessToken()
    idToken = getIdToken()
    return unreal.PlugoonTokens(id_token=idToken, access_token=accessToken)