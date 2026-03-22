class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #### MY SOLUTION (I think my solution is great) ####
        
        # left = 0 #We will consider left to remove the characters
        # right = 0 #we will consider right to add characters

        # char_dict = {} #this will track if the window contains any duplicates
        # longest_sub = 0 # this will be the output i.e, it will track the longest substring

        # while left <= len(s)-1 and right <= len(s)-1: #checking only 'right' because if right exceeds the end without being duplicate then we r done

        #     #There are 2 conditions : Either character will be present in the hashmap or it won't
        #     if s[right] not in char_dict.keys() or char_dict[s[right]] == 0:
        #         char_dict[s[right]] = 1 #add to the frequency list
        #         length_of_window = right - left + 1
        #         longest_sub = max(longest_sub, length_of_window)
        #         right += 1
        #     elif char_dict[s[right]] == 1 : #we will move left pointer until s[right] other dublicates are removed and s[right] becomes unique again
        #         char_dict[s[left]] -= 1 #reduce the frequency of the char in hashmap
        #         left += 1
        
        # return longest_sub


        #### NEETCODE SOLUTION #####

        charset = set()

        longest_sub = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            
            charset.add(s[r])
            window_size = r - l + 1
            longest_sub = max(longest_sub, window_size)
        
        return longest_sub
            
