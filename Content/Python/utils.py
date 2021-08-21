import unreal
import json

def get_unreal_version() -> str:
    with open(unreal.Paths.get_project_file_path(), "r") as f:
        return json.loads(f.read())["EngineAssociation"]