import unittest
import sum_of_scores

class TestTwoSums(unittest.TestCase):

    def test_1(self):
        sol = sum_of_scores.Solution()
        result = sol.scoreOfString("zaz")
        self.assertEqual(result, 50)
        self.assertIsInstance(result, int)
    
    def test_2(self):
        sol = sum_of_scores.Solution()
        result = sol.scoreOfString("hello")
        self.assertEqual(result, 13)
        self.assertIsInstance(result, int)


    if __name__ == "__main__":
        unittest.main()