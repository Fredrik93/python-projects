from leetcode.min_bit_flips import MinFlips

def test_basic_case():
    solution = MinFlips()
    assert solution.minBitFlips(10,7) == 3


def test_basic_case2():
    solution = MinFlips()
    assert solution.minBitFlips(3,4) == 3