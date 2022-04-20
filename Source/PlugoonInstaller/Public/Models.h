#pragma once

#include "CoreMinimal.h"

#include "Models.generated.h"

USTRUCT(BlueprintType)
struct FPlugoonTokens
{
	GENERATED_BODY();

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	FString IdToken;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	FString AccessToken;
};

USTRUCT(BlueprintType)
struct FPlugoonRepo
{
	GENERATED_BODY();

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	FString Name;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	FString Owner;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	FString Description;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	TArray<FString> UeVersions;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	TArray<FString> Packages;
};

USTRUCT(BlueprintType)
struct FPlugoonPackage
{
	GENERATED_BODY();
	
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	FString Id;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	FString RepoName;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	FString UeVersion;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	FString PackageVersion;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	FString Url;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	bool Deprecated;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	TArray<FString> Dependencies;
};

USTRUCT(BlueprintType)
struct FPlugoonError
{
	GENERATED_BODY();

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	bool HasError;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	FString Message;
};

USTRUCT(BlueprintType)
struct FPlugoonRepoResponse
{
	GENERATED_BODY();

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	FPlugoonError Error;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	FPlugoonRepo Repo;
};

USTRUCT(BlueprintType)
struct FPlugoonPackageResponse
{
	GENERATED_BODY();

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	FPlugoonError Error;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	FPlugoonPackage Package;
};

USTRUCT(BlueprintType)
struct FPlugoonReposResponse
{
	GENERATED_BODY();

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	FPlugoonError Error;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	TArray<FPlugoonRepo> Repos;
};

USTRUCT(BlueprintType)
struct FPlugoonPackagesResponse
{
	GENERATED_BODY();

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	FPlugoonError Error;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category=Plugoon)
	TArray<FPlugoonPackage> Packages;
};