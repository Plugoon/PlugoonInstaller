from __future__ import annotations
import unreal

class Test:
    def __init__(self) -> None:
        self.success: int = 0
        self.fail: int = 0
        self.total: int = 0
        self.testInstances: list[Test] = []
        self.protocol: list[str] = []

    def add(self, instance: Test):
        self.testInstances.append(instance)

    def run(self):
        self.protocol.append("==============================")
        self.protocol.append("Test protocol")
        self.protocol.append("==============================")
        self.protocol.append("------------------------------")
        if len(self.testInstances) == 0:
            self.protocol.append("no tests")
            return
        for instance in self.testInstances:
            self._run_instance_tests(instance)
            self.protocol.append("------------------------------")

    def result(self):
        self.protocol.append("==============================")
        self.protocol.append(f"Tests run: {self.total}")
        self.protocol.append(f"Success: {self.success}")
        self.protocol.append(f"Fail: {self.fail}")
        self.protocol.append("==============================")
        for entry in self.protocol:
            unreal.log(entry)

    def _run_instance_tests(self, instance: Test):
        testMethods: list[str] = [method for method in dir(instance.__class__) if method.startswith('test_') is True]
        self.protocol.append(f"Run tests for {instance.__class__.__name__}:")
        for test in testMethods:
            self.total += 1
            try:
                getattr(instance, test)()
                self.success += 1
                self.protocol.append(f"Success: {instance.__class__.__name__} -> {test}")
            except:
                self.fail += 1
                self.protocol.append(f"Fail:    {instance.__class__.__name__} -> {test}")