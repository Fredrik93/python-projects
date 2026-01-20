import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0,1], p=[1-p1, p1], size=10000)
    return seq

def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    countOnes = 0
    occurrencesOfOnes = 0
    for num in seq:
        if num == 1:
            countOnes = countOnes +1
        else:
            countOnes = 0

        if (countOnes == 5):
            occurrencesOfOnes = occurrencesOfOnes +1
            countOnes = 4
    
    return occurrencesOfOnes 

def main(p1):
    seq = generate(p1)
    res = count(seq)
    return res
print("helo")
print(main(2/3))
