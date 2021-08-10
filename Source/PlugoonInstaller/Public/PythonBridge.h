#pragma once
#include "Engine.h"
#include "PythonBridge.generated.h"

UCLASS(Blueprintable)
class UPythonBridge: public UObject
{
	GENERATED_BODY()
public:
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
    FString Test();
	
	UFUNCTION(BlueprintCallable, Category=Python)
	static UPythonBridge* Get();

	UFUNCTION(BlueprintImplementableEvent, Category=Python)
	void StartInstaller() const;
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	TArray<FString> GetPlugoonRepositories();

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	TMap<FString, FString> GetPlugoonRepositoriesDetails(const FString& Repo);

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
    bool SetPlugoonToken(const FString& Token);

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
    FString GetPlugoonToken();

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
    TArray<FString> GetInstalledPlugins();

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
    TMap<FString, FString> GetInstalledPluginDetails(const FString& Handle);
};
