#pragma once
#include "Engine.h"
#include "Models/PlugoonTokens.h"

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
	void SetTokens(const FString& IdToken, const FString& AccessToken);

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonTokens GetTokens();
    
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
    FString GetUnrealVersion();
};
