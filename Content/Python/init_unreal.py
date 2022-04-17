from typing import overload
import unreal
import utils
import TokenLib
import requests

@unreal.uclass()
class EditorUtility(unreal.EditorUtilitySubsystem):
    pass

@unreal.uclass()
class PythonBridgeImplementation(unreal.PythonBridge):

    @unreal.ufunction(override=True)
    def test(self):
        unreal.log("Test")
        return ""


    # Editor startup function
    @unreal.ufunction(override=True)
    def start_installer(self):
        PlugoonStartup = unreal.load_asset('/PlugoonInstaller/Widgets/PlugoonInstaller.PlugoonInstaller')
        EditorUtility().spawn_and_register_tab(PlugoonStartup)

    @unreal.ufunction(override=True)
    def set_tokens(self, idToken, accessToken):
        idToken = TokenLib.setIdToken(idToken)
        accessToken = TokenLib.setAccessToken(accessToken)
        return (idToken & accessToken)

    @unreal.ufunction(override=True)
    def get_tokens(self):
        return TokenLib.getTokens()

    @unreal.ufunction(override=True)
    def get_unreal_version(self):
        return utils.get_unreal_version()

    @unreal.ufunction(override=True)
    def get_repos(self):
        return requests.get_repos()

    @unreal.ufunction(override=True)
    def add_repo(self, name, description):
        return requests.add_repo(name, description)

    @unreal.ufunction(override=True)
    def update_repo(self, name, description):
        return requests.update_repo(name, description)

    @unreal.ufunction(override=True)
    def delete_repo(self, name):
        return requests.delete_repo(name)

    @unreal.ufunction(override=True)
    def get_packages(self, name):
        return requests.get_packages(name)

    @unreal.ufunction(override=True)
    def add_package(self, name, ue_version, package_version, url, dependencies):
        return requests.add_package(name, ue_version, package_version, url, dependencies)

    @unreal.ufunction(override=True)
    def get_package(self, name, package_id):
        return requests.get_package(name, package_id)

    @unreal.ufunction(override=True)
    def update_package(self, name, package_id, url):
        return requests.update_package(name, package_id, url)

    @unreal.ufunction(override=True)
    def deprecate_package(self, name, package_id):
        return requests.deprecate_package(name, package_id)

    @unreal.ufunction(override=True)
    def delete_package(self, name, package_id):
        return requests.delete_package(name, package_id)

    @unreal.ufunction(override=True)
    def get_install_list(self, name, package_id):
        return requests.get_install_list(name, package_id)