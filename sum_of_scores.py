class Solution:
    def scoreOfString (self, s: str) -> int:
        result = 0
        for i in range(len(s)-1):
            currChar = ord(s[i])
            nextChar = ord(s[i+1])
            result += abs(currChar - nextChar)       
        return result