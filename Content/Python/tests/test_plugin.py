from plugin import Plugin
from tests.helper import Test
import unittest

class Test_Plugin(unittest.TestCase):
    def test_get_installed_plugins(self):
        plugins = Plugin.get_installed_plugins()
        for plugin in plugins:
            if plugin.name == "PlugoonInstaller":
                self.assertTrue(True)
                return
        self.assertTrue(False)
    
    def test_get_installed_plugins_count(self):
        self.assertGreater(len(Plugin.get_installed_plugins()), 0)

if __name__ == '__main__':
    test = Test()
    test.add(Test_Plugin())
    test.run()
    test.result()