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
	TArray<FString> GetMatchingPlugoonRepositories();

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	TMap<FString, FString> GetPlugoonRepositoryDetails(const FString& Repo);

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
    bool SetPlugoonToken(const FString& Token);

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
    FString GetPlugoonToken();

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
    TArray<FString> GetInstalledPlugins();

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
    TMap<FString, FString> GetInstalledPluginDetails(const FString& Handle);
    
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
    FString GetUnrealVersion();
};
