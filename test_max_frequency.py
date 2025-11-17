import unittest
import leetcode.max_frequency

class TestMaxFreqSum(unittest.TestCase):

    def test_returns_zero(self):
        obj = leetcode.max_frequency.MaxyMax()
        result = obj.maxFreqSum("successes")
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
