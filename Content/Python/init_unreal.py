import unreal
import utils
import TokenLib
import requests
import installer

@unreal.uclass()
class EditorUtility(unreal.EditorUtilitySubsystem):
    pass

@unreal.uclass()
class PythonBridgeImplementation(unreal.PythonBridge):

    @unreal.ufunction(override=True)
    def test(self):
        requests.download_file(
            "https://github.com/Plugoon/Core/archive/refs/tags/UE5.0-v1.0.zip",
            f"{unreal.Paths.project_plugins_dir()}/Download.zip"
        )


    @unreal.ufunction(override=True)
    def open_error(self):
        error = unreal.load_asset('/PlugoonInstaller/Widgets/EUW_Error.EUW_Error')
        return EditorUtility().spawn_and_register_tab(error)

    @unreal.ufunction(override=True)
    def open_widget(self, link):
        widget = unreal.load_asset(link)
        return EditorUtility().spawn_and_register_tab(widget)

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
    def get_repos(self, version):
        return requests.get_repos(version)

    @unreal.ufunction(override=True)
    def get_owned_repos(self):
        return requests.get_owned_repos()

    @unreal.ufunction(override=True)
    def add_repo(self, name, description, repo_link, documentation, support):
        return requests.add_repo(name, description, repo_link, documentation, support)

    @unreal.ufunction(override=True)
    def update_repo(self, name, description, repo_link, documentation, support):
        return requests.update_repo(name, description, repo_link, documentation, support)

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

    @unreal.ufunction(override=True)
    def install_packages(self, packages):
        return installer.install_plugins(packages)

    @unreal.ufunction(override=True)
    def get_installed_packages(self):
        return installer.get_installed_packages()

    @unreal.ufunction(override=True)
    def get_newest_package(self, packages, ue_version):
        return utils.get_newest_package(packages, ue_version)