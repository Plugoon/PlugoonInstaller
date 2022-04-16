#pragma once
#include "Engine.h"
#include "Models.h"

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

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	TArray<FPlugoonRepo> GetRepos();

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonRepo AddRepo(const FString& Name, const FString& Description);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonRepo UpdateRepo(const FString& Name, const FString& Description);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	void DeleteRepo(const FString& Name);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	TArray<FPlugoonPackage> GetPackages(const FString& Name);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonPackage AddPackage(
		const FString& Name,
		const FString& PackageVersion,
		const FString& Url,
		const TArray<FString>& Dependencies
	);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonPackage GetPackage(const FString& Name, const FString& PackageId);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonPackage UpdatePackage(
		const FString& Name,
		const FString& PackageId,
		const FString& Url
	);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonPackage DeprecatePackage(
		const FString& Name,
		const FString& PackageId
	);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	void DeletePackage(
		const FString& Name,
		const FString& PackageId
	);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)	
	TArray<FPlugoonPackage> GetInstallList(
		const FString& Name,
		const FString& PackageId
	);
};
