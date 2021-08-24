from datetime import datetime
import unreal
import PlugoonLibrary as lib
from organization import Organization
import plugin

@unreal.uclass()
class EditorUtility(unreal.EditorUtilitySubsystem):
    pass

@unreal.uclass()
class PythonBridgeImplementation(unreal.PythonBridge):

    @unreal.ufunction(override=True)
    def test(self):
        unreal.log("Test")

    @unreal.ufunction(override=True)
    def start_installer(self):
        PlugoonStartup = unreal.load_asset('/PlugoonInstaller/Widgets/PlugoonInstaller.PlugoonInstaller')
        EditorUtility().spawn_and_register_tab(PlugoonStartup)

    @unreal.ufunction(override=True)
    def get_matching_plugoon_repositories(self):
        org = Organization("Plugoon").get_matching_repos()
        return org["data"].keys()

    @unreal.ufunction(override=True)
    def get_plugoon_repository_details(self, repo):
        return Organization("Plugoon").get_matching_repos()["data"][repo]

    @unreal.ufunction(override=True)
    def set_plugoon_token(self, token):
        return lib.SetPrivateRepoToken(token)

    @unreal.ufunction(override=True)
    def get_plugoon_token(self):
        return lib.GetPrivateRepoToken()

    @unreal.ufunction(override=True)
    def get_unreal_version(self):
        return lib.GetUnrealVersion()