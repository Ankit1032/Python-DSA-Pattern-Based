class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): #if len of 's' is not same as 't'
            return False
            
        freq_dict_c = {}

        for c in s:
            if c not in freq_dict_c.keys(): 
                freq_dict_c[c] = 1
            else:
                freq_dict_c[c] += 1

        for c in t:
            if c not in freq_dict_c.keys(): #a character from 't' is not present in 's'
                return False
            elif c in freq_dict_c.keys() and freq_dict_c[c] == 0: #a character is 't' occurs more than it occurs in 's'
                return False
            else:
                freq_dict_c[c] -= 1

        if sum(freq_dict_c.values()) == 0: # as we subtract the frequency of 't' from 'c', if the values of the dict ain't 0 then its not anagram
            return True
        
        return False
        
