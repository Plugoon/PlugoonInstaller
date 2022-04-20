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
	UObject* OpenError();

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	UObject* OpenWidget(const FString& Link);

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	void SetTokens(const FString& IdToken, const FString& AccessToken);

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonTokens GetTokens();
    
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
    FString GetUnrealVersion();

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonReposResponse GetRepos(const FString& Version);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonReposResponse GetOwnedRepos();

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonRepoResponse AddRepo(const FString& Name, const FString& Description);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonRepoResponse UpdateRepo(const FString& Name, const FString& Description);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonError DeleteRepo(const FString& Name);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonPackagesResponse GetPackages(const FString& Name);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonPackageResponse AddPackage(
		const FString& Name,
		const FString& UeVersion,
		const FString& PackageVersion,
		const FString& Url,
		const TArray<FString>& Dependencies
	);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonPackageResponse GetPackage(const FString& Name, const FString& PackageId);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonPackageResponse UpdatePackage(
		const FString& Name,
		const FString& PackageId,
		const FString& Url
	);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonPackageResponse DeprecatePackage(
		const FString& Name,
		const FString& PackageId
	);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonError DeletePackage(
		const FString& Name,
		const FString& PackageId
	);
	
	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)	
	FPlugoonPackagesResponse GetInstallList(
		const FString& Name,
		const FString& PackageId
	);

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonError InstallPackages(const TArray<FPlugoonPackage>& Packages);

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonPackagesResponse GetInstalledPackages();

	UFUNCTION(BlueprintImplementableEvent, BlueprintCallable, Category=Python)
	FPlugoonPackageResponse GetNewestPackage(const TArray<FPlugoonPackage>& Packages, const FString& UeVersion);
};
