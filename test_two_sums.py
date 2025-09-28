import unittest
import leetcode.two_sums as two_sums

class TestTwoSums(unittest.TestCase):

    def test_1(self):
        sol = two_sums.Twosum()
        result = sol.twoSum([3,2,3],6)
        self.assertEqual(result, [0,2])
        self.assertIsInstance(result, list)

    def test_2(self):
        sol = two_sums.Twosum()
        result = sol.twoSum([2, 7,11,15],9)
        self.assertEqual(result, [0,1])
        self.assertIsInstance(result, list)

    def test_3(self):
        sol = two_sums.Twosum()
        result = sol.twoSum([2,11,15,7],18)
        self.assertEqual(result, [1,3])
        self.assertIsInstance(result, list)

    if __name__ == "__main__":
        unittest.main()