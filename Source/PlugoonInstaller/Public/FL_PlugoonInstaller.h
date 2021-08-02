// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"

#include "PythonBridge.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "FL_PlugoonInstaller.generated.h"

/**
 * 
 */
UCLASS()
class PLUGOONINSTALLER_API UFL_PlugoonInstaller : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()

public:
	UFUNCTION(BlueprintPure , Category="Plugoon|Installer")
	static UPythonBridge* GetPythonBridge();
};
