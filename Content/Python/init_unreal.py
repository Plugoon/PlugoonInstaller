import unreal
import utils
import TokenLib
import backend

@unreal.uclass()
class EditorUtility(unreal.EditorUtilitySubsystem):
    pass

@unreal.uclass()
class PythonBridgeImplementation(unreal.PythonBridge):

    @unreal.ufunction(override=True)
    def test(self):
        unreal.log("Test")
        backend.test()
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