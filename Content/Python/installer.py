import json
import unreal
from urllib import request
import os
import os.path
import utils
import requests
import shutil
import glob

pluginFolder = unreal.Paths.project_plugins_dir()
tempFolder = f"{pluginFolder}temp"

def install_plugins(list: list[unreal.PlugoonPackage]):
    utils.log("install_plugins", "install plugins started...")
    deprecated = False
    notFound = False
    if not os.path.exists(tempFolder):
        os.makedirs(tempFolder)
    total_frames = len(list) * 2
    text_label = "Install Plugins!"
    with unreal.ScopedSlowTask(total_frames, text_label) as install_task:
        install_task.make_dialog(True)
        for i in range(len(list)):
            if install_task.should_cancel():
                break
            filename = f"{list[i].repo_name}-UE{list[i].ue_version}-v{list[i].package_version}"
            temp_file = f"{tempFolder}/{filename}.zip"
            if not os.path.isfile(temp_file):
                utils.log("install_plugins", f"Package: {filename}")
                try:
                    requests.download_file(list[i].url, temp_file)
                except:
                    notFound = True
                    install_task.enter_progress_frame(2)
                    break
            install_task.enter_progress_frame(1)

            plugin_folder = f"{pluginFolder}{filename}"
            if not os.path.exists(plugin_folder):
                os.makedirs(plugin_folder)
                shutil.unpack_archive(temp_file, plugin_folder)
                config = {
                    "id": list[i].id,
                    "repo_name": list[i].repo_name,
                    "ue_version": list[i].ue_version,
                    "package_version": list[i].package_version,
                    "url": list[i].url,
                    "deprecated": list[i].deprecated
                }
                if list[i].deprecated == True:
                    deprecated = True
                with open(f"{plugin_folder}/config.plugoon", "w") as f:
                    f.write(json.dumps(config, indent=4))
            install_task.enter_progress_frame(1)
    shutil.rmtree(tempFolder)
    if notFound:
        return unreal.PlugoonError(
            has_error=True,
            message="Could not find every Package. Package may not be working as intended"
        )
    if deprecated:
        return unreal.PlugoonError(
            has_error=True,
            message="Some installed packages are deprecated. Package may not be working as intended"
        )
    return unreal.PlugoonError()

def get_installed_packages():
    files = glob.glob(pluginFolder + "**/config.plugoon", recursive=True)
    result = []
    for file in files:
        with open(file, "r") as f:
            obj = json.loads(f.read())
            result.append(unreal.PlugoonPackage(
                id=obj["id"],
                repo_name=obj["repo_name"],
                ue_version=obj["ue_version"],
                package_version=obj["package_version"],
                url=obj["url"],
                deprecated=obj["deprecated"]
            ))
    return unreal.PlugoonPackagesResponse(packages=result)
            
    