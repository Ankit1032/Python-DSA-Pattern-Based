class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransom_char_dict = {}

        for i in ransomNote:
            ransom_char_dict[i] = 1 + ransom_char_dict.get(i,0)

        for i in magazine:
            if i in ransom_char_dict.keys() and ransom_char_dict[i] > 0:
                ransom_char_dict[i] -= 1
        
        return sum(ransom_char_dict.values()) == 0
