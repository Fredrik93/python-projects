from leetcode.reverse_prefix_string import RevPref
# this is the way to write tests when we use a class in python. like in this case. you need to import the class RevPref.
# see test_two_sum.py for another example of not using a class

def test_basic_case():
    solution = RevPref()
    assert solution.reversePrefix("abcd",2) == "bacd"

def test_basic_case_2():
    assert reversePrefix("xyz", 3) == "zyx"