class MaxyMax:
    def maxFreqSum(self, s: str) -> int:
        mostFrequentVowel = 0
        mostFrequentConsonant = 0
        vowels = "aoeiu"
        # save currentChar 
        for currentCharacter in s:
            occurencesOfCurrentCharacter = 0
            for character in s:
                if currentCharacter == character:
                    occurencesOfCurrentCharacter = occurencesOfCurrentCharacter +1
            if currentCharacter in vowels:
                if occurencesOfCurrentCharacter > mostFrequentVowel:
                    mostFrequentVowel = occurencesOfCurrentCharacter
            else:
                if occurencesOfCurrentCharacter > mostFrequentConsonant:
                    mostFrequentConsonant = occurencesOfCurrentCharacter 
        return mostFrequentVowel + mostFrequentConsonant
        