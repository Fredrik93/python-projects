import string
class ReverseDegree:
    def reverseDegree(self, s: str) -> int:
        # create reversed arr of alphabet 
        alphabet = list(reversed(string.ascii_lowercase))
        result = 0
        print(alphabet)
        # for each char in a loop over string s, grab the matching chars index 
        for letter in s:
            for char in alphabet:
                if letter == char:
                    print(f"letter is {letter}, with index {alphabet.index(char)}")
                    # adding a one because list starts at 0 not at 1 
                    result = result + alphabet.index(char) + 1
                
            
        # add to total 
        # return total 
        return result
     