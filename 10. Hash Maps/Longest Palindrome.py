class Solution:
    def longestPalindrome(self, s: str) -> int:

        #My intuition was
        # 1. even letters can always be arranged as palindrome so just count the letters with even occurance
        # 2. odd occuring letters are tricky, even tho we have multiple odd letters, we can only use the odd letters in our palindrome (without center position) if there occurance is 3 or more
        # example: cccbbbbddd --> palindrome: dcbbcbbcd --> here in center we can put either 'c' or 'd' as odd number allows us too but we cannot put all odd numbers so when we count odd letters, we count using v-1 as 1 letter in it will always get wasted
        # 4. At the end , we add +1 to count the one of the wasted odd letters to position in center
        
        char_dict = {}
        for i in range(len(s)):
            char_dict[s[i]] = 1 + char_dict.get(s[i], 0)
        
        even_letters_count = 0
        odd_letter_count_len = 0
        odd = 0
        
        for k,v in char_dict.items():
            if v%2 == 0:
                even_letters_count += v
            else:
                odd_letter_count_len += (v-1)
                odd += 1

        if  odd > 0:
            odd_letter_count_len += 1

        return even_letters_count + odd_letter_count_len
