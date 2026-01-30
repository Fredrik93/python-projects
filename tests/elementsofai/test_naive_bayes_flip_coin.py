from elementsofai.naive_bayes_flip_coin import bayes, roll

def testOk():
    sequence = roll(True)
    res = bayes(sequence)
    assert(res == True)

def testOk1():
    sequence = roll(False)
    res = bayes(sequence)
    assert(res == False)