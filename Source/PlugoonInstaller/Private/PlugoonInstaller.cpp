// Copyright Epic Games, Inc. All Rights Reserved.

#include "PlugoonInstaller.h"
#include "PlugoonInstallerStyle.h"
#include "PlugoonInstallerCommands.h"
#include "PythonBridge.h"
#include "Misc/MessageDialog.h"
#include "ToolMenus.h"

static const FName PlugoonInstallerTabName("PlugoonInstaller");

#define LOCTEXT_NAMESPACE "FPlugoonInstallerModule"

void FPlugoonInstallerModule::StartupModule()
{
	// This code will execute after your module is loaded into memory; the exact timing is specified in the .uplugin file per-module
	
	FPlugoonInstallerStyle::Initialize();
	FPlugoonInstallerStyle::ReloadTextures();

	FPlugoonInstallerCommands::Register();
	
	PluginCommands = MakeShareable(new FUICommandList);

	PluginCommands->MapAction(
		FPlugoonInstallerCommands::Get().PluginAction,
		FExecuteAction::CreateRaw(this, &FPlugoonInstallerModule::PluginButtonClicked),
		FCanExecuteAction());

	UToolMenus::RegisterStartupCallback(FSimpleMulticastDelegate::FDelegate::CreateRaw(this, &FPlugoonInstallerModule::RegisterMenus));
}

void FPlugoonInstallerModule::ShutdownModule()
{
	// This function may be called during shutdown to clean up your module.  For modules that support dynamic reloading,
	// we call this function before unloading the module.

	UToolMenus::UnRegisterStartupCallback(this);

	UToolMenus::UnregisterOwner(this);

	FPlugoonInstallerStyle::Shutdown();

	FPlugoonInstallerCommands::Unregister();
}

void FPlugoonInstallerModule::PluginButtonClicked()
{
	UPythonBridge* Bridge = UPythonBridge::Get();
	Bridge->FunctionImplementedInPython();
}

void FPlugoonInstallerModule::RegisterMenus()
{
	// Owner will be used for cleanup in call to UToolMenus::UnregisterOwner
	FToolMenuOwnerScoped OwnerScoped(this);

	{
		UToolMenu* Menu = UToolMenus::Get()->ExtendMenu("LevelEditor.MainMenu.Window");
		{
			FToolMenuSection& Section = Menu->FindOrAddSection("WindowLayout");
			Section.AddMenuEntryWithCommandList(FPlugoonInstallerCommands::Get().PluginAction, PluginCommands);
		}
	}

	{
		UToolMenu* ToolbarMenu = UToolMenus::Get()->ExtendMenu("LevelEditor.LevelEditorToolBar");
		{
			FToolMenuSection& Section = ToolbarMenu->FindOrAddSection("Settings");
			{
				FToolMenuEntry& Entry = Section.AddEntry(FToolMenuEntry::InitToolBarButton(FPlugoonInstallerCommands::Get().PluginAction));
				Entry.SetCommandList(PluginCommands);
			}
		}
	}
}

#undef LOCTEXT_NAMESPACE
	
IMPLEMENT_MODULE(FPlugoonInstallerModule, PlugoonInstaller)