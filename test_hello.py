import unittest
import hello
class test_hello(unittest.TestCase):
    def test_add(self):
        self.assertEqual(hello.add(2,3), 5)
        self.assertEqual(hello.add(-1,1),0)