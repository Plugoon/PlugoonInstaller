#pragma once
#include "Engine.h"
#include "PythonBridge.generated.h"

UCLASS(Blueprintable)
class UPythonBridge: public UObject
{
	GENERATED_BODY()
public:
	UFUNCTION(BlueprintCallable, Category=Python)
	static UPythonBridge* Get();

	UFUNCTION(BlueprintImplementableEvent, Category=Python)
	void FunctionImplementedInPython() const;
};
