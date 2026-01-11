class RevPref:

    def reversePrefix(self, s:str, k: int) -> str:
        # get the kth substring of the string 
        subString = s[0:k]
        restOfTheString = s[k:]
        # get the rest of the string (kth - string length)
        # reverse the substring
        # concaternate the end of the string to the reversed substring
        # return value 
        return "hi"