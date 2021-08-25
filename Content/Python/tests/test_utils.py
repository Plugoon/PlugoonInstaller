import utils
import unittest
from tests.helper import Test

class Test_Utils(unittest.TestCase):
    def test_get_unreal_version(self):
        self.assertEqual(utils.get_unreal_version(), "5.0")

if __name__ == '__main__':
    test = Test()
    test.add(Test_Utils())
    test.run()
    test.result()
