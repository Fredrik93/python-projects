import unittest
from leetcode.reverse_string_prefix import reversePrefix

class TestRev(unittest.TestCase):
    def test_1(self):
        obj = reversePrefix()
        result = obj.reversePrefix("abcde", 2)
        self.assertEqual(result, "bacde")

if __name__ == "__main__":
    unittest.main()
