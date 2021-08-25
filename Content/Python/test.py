from __future__ import annotations
import unittest
import unreal
from plugin import Plugin

class Test:
    success: int = 0
    fail: int = 0
    total: int = 0
    testInstances: list[Test] = []

    def add(self, instance: Test):
        self.testInstances.append(instance)

    def run(self):
        unreal.log("------------------------------")
        unreal.log("Run tests")
        unreal.log("------------------------------")
        for instance in self.testInstances:
            self._run_instance_tests(instance)

    def result(self):
        unreal.log("------------------------------")
        unreal.log(f"Tests run: {self.total}")
        unreal.log(f"Success: {self.success}")
        unreal.log(f"Fail: {self.fail}")
        unreal.log("------------------------------")

    def _run_instance_tests(self, instance: Test):
        testMethods: list[str] = [method for method in dir(instance.__class__) if method.startswith('test_') is True]
        unreal.log(f"Run tests for {instance.__class__.__name__}")
        for test in testMethods:
            self.total += 1
            try:
                getattr(instance, test)()
                self.success += 1
                unreal.log(f"Success: {instance.__class__.__name__}-> {test}")
            except:
                self.fail += 1
                unreal.log_error(f"  {instance.__class__.__name__}-> {test}")
        
test = Test()
# test.add(MyTest())
test.run()
test.result()

