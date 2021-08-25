from tests.helper import Test
from tests.test_plugin import Test_Plugin
from tests.test_utils import Test_Utils

if __name__ == '__main__':
    test = Test()
    test.add(Test_Plugin())
    test.add(Test_Utils())
    test.run()
    test.result()

