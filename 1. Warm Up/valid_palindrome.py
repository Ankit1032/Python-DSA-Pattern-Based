class Solution:
    def isPalindrome(self, s: str) -> bool:
        fresh_s = ""

        for c in s:
            if c.isalnum():
                fresh_s += c.lower() #concatenate

        #palidrome
        if fresh_s == fresh_s[::-1]:
            return True
        
        return False
        
