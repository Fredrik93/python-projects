import unittest
import leetcode.sum_of_xor_subsets as subsets

class TestXORTotal(unittest.TestCase):

    def test_1(self):
        
        result = subsets.Total([1,3])
        self.assertEqual(result, 6)

    def test_2(self):
        
        result = subsets.Total([5,1,6])
        self.assertEqual(result, 28)

if __name__ == "__main__":
        unittest.main()