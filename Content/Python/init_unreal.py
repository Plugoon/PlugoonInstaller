import unreal
import PlugoonLibrary as lib

@unreal.uclass()
class EditorUtility(unreal.EditorUtilitySubsystem):
    pass

@unreal.uclass()
class PythonBridgeImplementation(unreal.PythonBridge):

    @unreal.ufunction(override=True)
    def test(self):
        return lib.GetInstalledPlugins()


    @unreal.ufunction(override=True)
    def start_installer(self):
        PlugoonStartup = unreal.load_asset('/PlugoonInstaller/Widgets/PlugoonInstaller.PlugoonInstaller')
        EditorUtility().spawn_and_register_tab(PlugoonStartup)

    @unreal.ufunction(override=True)
    def get_plugoon_repositories(self):
        return lib.GetPlugoonRepo()

    @unreal.ufunction(override=True)
    def get_plugoon_repositories_details(self, repo):
        return lib.GetPlugoonRepoDetails(repo)

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