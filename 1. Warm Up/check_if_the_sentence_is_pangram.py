class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        freq_sen = {}

        for c in sentence:
            c = c.lower()

            if c.isalpha() and c not in freq_sen.keys():
                freq_sen[c] = 1

        if sum(freq_sen.values()) == 26:
            return True
        else:
            return False
