import unreal
import json
import os
from datetime import datetime
import json

tempPath = f"{unreal.Paths.project_plugins_dir()}PlugoonInstaller/Temp"

def log(method: str, message: str):
    unreal.log(f"Plugoon Installer: {method} -> {message}")

def log_warning(method: str, message: str):
    unreal.log_warning(f"Plugoon Installer: {method} -> {message}")

def log_error(method: str, message: str):
    unreal.log_error(f"Plugoon Installer: {method} -> {message}")

def get_unreal_version() -> str:
    with open(unreal.Paths.get_project_file_path(), "r") as f:
        return json.loads(f.read())["EngineAssociation"]

def save_organization_details(data: dict) -> None:
    log("save_organization_details", "start...")
    try:
        if not os.path.exists(tempPath):
            os.makedirs(tempPath)
        unreal.log(data)
        # with open(f"{tempPath}/organization.json", "w") as f:
        #     f.write(json.dumps(save.__dict__))
    except:
        log_error("save_organization_details", "could not write to organization.json")
