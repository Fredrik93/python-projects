class RevPref:

    def reversePrefix(self, s:str, k: int) -> str:
        # get the kth substring of the string 
        subString = s[0:k]
        # get the rest of the string (kth - string length)
        restOfTheString = s[k:]
        # reverse the substring
        rev = subString[::-1]
        # concaternate the end of the string to the reversed substring
        res = rev + restOfTheString
        # return value 
        return res