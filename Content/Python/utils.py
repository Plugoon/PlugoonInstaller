import unreal
import json
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
