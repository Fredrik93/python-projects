

def bot8(pbot, p8_bot, p8_human):
    prob_of_8digits = calculateP8Digits(pbot, p8_bot, p8_human)
    print(prob_of_8digits)
    probBotGiven8Digits = calculateProbOfBeingABotUser(prob_of_8digits, p8_bot, pbot)
    print(prob_of_8digits)
    return probBotGiven8Digits

def calculateP8Digits(pbot, p8_bot, p8_human):
    phuman = 1 - pbot 
    prob = (p8_bot * pbot) + (p8_human * phuman)
    return prob

def calculateProbOfBeingABotUser(prob_of_8_digits, p8_bot, pbot):
    prob8DigitsGivenBot = p8_bot * pbot
    probBotGiven8Digits = prob8DigitsGivenBot / prob_of_8_digits
    return probBotGiven8Digits




