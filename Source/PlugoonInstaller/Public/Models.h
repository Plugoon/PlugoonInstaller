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