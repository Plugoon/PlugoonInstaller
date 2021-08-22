import unreal
import PlugoonLibrary as lib
import github as git

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
        return git.get_matching_plugoon_repos().keys()

    @unreal.ufunction(override=True)
    def get_plugoon_repository_details(self, repo):
        return git.get_matching_plugoon_repos()[repo]

    @unreal.ufunction(override=True)
    def set_plugoon_token(self, token):
        return lib.SetPrivateRepoToken(token)

    @unreal.ufunction(override=True)
    def get_plugoon_token(self):
        return lib.GetPrivateRepoToken()

    @unreal.ufunction(override=True)
    def get_installed_plugins(self):
        return lib.GetInstalledPlugins()

    @unreal.ufunction(override=True)
    def get_installed_plugin_details(self, handle):
        return lib.GetInstalledPluginDetails(handle)

    @unreal.ufunction(override=True)
    def get_unreal_version(self):
        return lib.GetUnrealVersion()