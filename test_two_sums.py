import unittest
import leetcode.two_sums as two_sums

class TestTwoSums(unittest.TestCase):

    def test_1(self):
        sol = two_sums.Twosum()
        result = sol.twoSum([3,3],6)
        self.assertEqual(result, [0,1])
        self.assertIsInstance(result, list)

    if __name__ == "__main__":
        unittest.main()