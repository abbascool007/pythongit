import unittest
#we are giving demo1 file name which we are taking data and giving the class we created in that file.
from demo1 import Sample1

#By default we need to specify the below 1st line
class MyTestCase(unittest.TestCase):
    def test_addingNumbers(self):
        Sample1.add(self,3,7)

    def test_subNumbers(self):
        Sample1.sub(self,5,4)
#if __name__ == '__main__':
#   unittest.main()
