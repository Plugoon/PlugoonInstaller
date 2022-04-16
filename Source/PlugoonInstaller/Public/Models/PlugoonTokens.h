#pragma once

#include "CoreMinimal.h"

#include "PlugoonTokens.generated.h"

USTRUCT(BlueprintType)
struct FPlugoonTokens
{
	GENERATED_BODY();

	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category=Plugoon)
	FString IdToken;

	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category=Plugoon)
	FString AccessToken;
};