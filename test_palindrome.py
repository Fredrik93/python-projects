import unittest
from palindrome import isPalindrome   # import function

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(isPalindrome(121))
        self.assertFalse(isPalindrome(-121))
        self.assertTrue(isPalindrome(1001))
        self.assertFalse(isPalindrome(123))

if __name__ == "__main__":
    unittest.main()
