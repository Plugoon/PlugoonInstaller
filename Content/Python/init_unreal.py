import unreal
import PlugoonLibrary as lib

@unreal.uclass()
class EditorUtility(unreal.EditorUtilitySubsystem):
    pass

@unreal.uclass()
class PythonBridgeImplementation(unreal.PythonBridge):

    @unreal.ufunction(override=True)
    def function_implemented_in_python(self):
        PlugoonStartup = unreal.load_asset('/PlugoonInstaller/Widgets/PlugoonInstaller.PlugoonInstaller')
        EditorUtility().spawn_and_register_tab(PlugoonStartup)

    @unreal.ufunction(override=True)
    def get_plugoon_repositories(self):
        return lib.GetPlugoonRepo()

    @unreal.ufunction(override=True)
    def get_plugoon_repositories_details(self, repo):
        return lib.GetPlugoonRepoDetails(repo)