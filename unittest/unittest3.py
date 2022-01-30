import unittest


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupclass will execute before test but only once")
        
    @classmethod
    def tearDownClass(cls):
        print("teardownclass will execute after all test")

    def test_add(self):
        print("test1")

    def test_sub(self):
        print("test2")