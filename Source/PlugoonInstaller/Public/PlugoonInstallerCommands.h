// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Framework/Commands/Commands.h"
#include "PlugoonInstallerStyle.h"

class FPlugoonInstallerCommands : public TCommands<FPlugoonInstallerCommands>
{
public:

	FPlugoonInstallerCommands()
		: TCommands<FPlugoonInstallerCommands>(TEXT("PlugoonInstaller"), NSLOCTEXT("Contexts", "PlugoonInstaller", "PlugoonInstaller Plugin"), NAME_None, FPlugoonInstallerStyle::GetStyleSetName())
	{
	}

	// TCommands<> interface
	virtual void RegisterCommands() override;

public:
	TSharedPtr< FUICommandInfo > PluginAction;
};
