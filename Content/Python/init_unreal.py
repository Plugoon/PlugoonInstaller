from tokenize import Token
import unreal
import PlugoonLibrary as lib
import TokenLib
from organization import Organization

@unreal.uclass()
class EditorUtility(unreal.EditorUtilitySubsystem):
    pass

@unreal.uclass()
class PythonBridgeImplementation(unreal.PythonBridge):

    @unreal.ufunction(override=True)
    def test(self):
        unreal.log("Test")

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
        return lib.GetUnrealVersion()