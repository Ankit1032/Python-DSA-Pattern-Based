class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)>len(s2):
            return False

        #we need to check if character of s2 is present in s1 but we need to make sure the frequency as one character, even tho present in s1 can have more continuous repetition as well

        #Creating a hashmap for s1 and s2 for length of s1 only.
        s1_hashmap = {}
        s2_hashmap = {}

        for i in range(len(s1)):
            s1_hashmap[s1[i]] = 1 + s1_hashmap.get(s1[i], 0)
            s2_hashmap[s2[i]] = 1 + s2_hashmap.get(s2[i], 0)
        
        
        if s1_hashmap == s2_hashmap:
            return True

        left = 0

        #we will only preserve s1 number of keys in s2, not necessary the same key but same number of keys so we can check
        #It is sliding a window over s2 of length s1
        for right in range(len(s1), len(s2)):
            s2_hashmap[s2[right]] = 1 + s2_hashmap.get(s2[right], 0)
            s2_hashmap[s2[left]] -= 1

            if s2_hashmap[s2[left]] == 0:
                del s2_hashmap[s2[left]]
            
            left += 1

            if s1_hashmap == s2_hashmap:
                return True

        return False


        
