class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        numString = str(x)
        reversed = numString[::-1]
        if x != int(reversed):
            return False
        return True
