class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        char_dict = {}

        for i in range(len(s)):
            char_dict[s[i]] = 1 + char_dict.get(s[i], 0)

        for i in range(len(s)):
            if char_dict[s[i]] == 1:
                return i
        
        return -1
