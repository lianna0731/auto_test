import unittest

class Add(unittest.TestCase):
    #def setUp(self):
        #pass
    #def tearDown(self):
        #pass
    def test_add(self):
        self.a=1
        self.b=2
        print(self.a+self.b+"测试")
