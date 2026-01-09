import string
class ReverseDegree:
    def reverseDegree(self, s: str) -> int:
        # create reversed arr of alphabet 
        alphabet = list(reversed(string.ascii_lowercase))
        result = 0
        print(alphabet)
        # for each char in a loop over string s, grab the matching chars index 
        for i, letter in enumerate(s):
            for char in alphabet:
                if letter == char:
                    print(f"letter is {letter}, with index {alphabet.index(char)} at {i+1}")
                    # adding a one because list starts at 0 not at 1 
                    index = i + 1
                    alphabetIndexValue = alphabet.index(char) +1
                    calculation = alphabetIndexValue * index
                    result = result + calculation
                
            
        # add to total 
        # return total 
        return result
     