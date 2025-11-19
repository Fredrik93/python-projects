import unittest
import leetcode.reverse_degree_of_string as rd

class TestRevDeg(unittest.TestCase):
    def test_1(self):
        obj = rd.ReverseDegree()
        result = obj.reverseDegree("ab")
        self.assertEqual(result, 51)
