// Copyright Epic Games, Inc. All Rights Reserved.

#include "PlugoonInstallerCommands.h"

#define LOCTEXT_NAMESPACE "FPlugoonInstallerModule"

void FPlugoonInstallerCommands::RegisterCommands()
{
	UI_COMMAND(PluginAction, "PlugoonInstaller", "Execute PlugoonInstaller action", EUserInterfaceActionType::Button, FInputGesture());
}

#undef LOCTEXT_NAMESPACE
