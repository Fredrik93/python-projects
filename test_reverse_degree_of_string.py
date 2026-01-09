import unittest
import leetcode.reverse_degree_of_string as rd

class TestRevDeg(unittest.TestCase):
    def test_1(self):
        obj = rd.ReverseDegree()
        result = obj.reverseDegree("ab")
        self.assertEqual(result, 126)

    def test_2(self):
        obj = rd.ReverseDegree()
        result = obj.reverseDegree("abc")
        self.assertEqual(result, 148)
    def test_3(self):
        obj = rd.ReverseDegree()
        result = obj.reverseDegree("zaza")
        self.assertEqual(result, 160)
