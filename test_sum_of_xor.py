import unittest
import leetcode.sum_of_xor_subsets as subsets

class TestTwoSums(unittest.TestCase):

    def test_1(self):
        
        result = subsets.Total([1,3])
        self.assertEqual(result, 6)

if __name__ == "__main__":
        unittest.main()