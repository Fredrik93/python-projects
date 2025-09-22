import unittest
from palindrome import Solution   # import function


class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_palindrome(self):
        self.assertTrue(self.s.isPalindrome(121))
        self.assertFalse(self.s.isPalindrome(-121))
        self.assertTrue(self.s.isPalindrome(1001))
        self.assertFalse(self.s.isPalindrome(123))

if __name__ == "__main__":
    unittest.main()
