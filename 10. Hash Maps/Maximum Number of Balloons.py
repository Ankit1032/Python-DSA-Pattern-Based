class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

    # My solution which failed for "balloonbaloonballoon" <- Important READ THIS
    # It failed as my solution assums the "balloon" doesn't have any duplicate character but it does 'l','o'
        # Intuition is to store the frequency of each char in text
        # then we will iterate through the word "balloon" and pick the minimum occuring keyword present here and that will be the number of times we can create the word balloon
        
        # char_dict = {}

        # for i in range(len(text)):
        #     char_dict[text[i]] = 1 + char_dict.get(text[i], 0)
        
        # s = "balloon"
        # min_rep = float('inf')

        # for i in s:
        #     min_rep = min(min_rep, char_dict.get(i, 0))
    
        #     #below conditions are present to handle if text = 'balon' as all letters are same as 'balloon' but this case is not succesful
        #     if i in char_dict.keys():
        #         char_dict[i] -= 1

        #         if char_dict[i] == 0:
        #             del char_dict[i]

        # # b = 3
        # # a = 3
        # # l = 5
        # # o = 6
        # # n = 3

        # # the above code will otuput 3 whereas it should be 2

        # return min_rep

        # My 2nd Solution
        text_char_dict = {}

        for i in range(len(text)):
            text_char_dict[text[i]] = 1 + text_char_dict.get(text[i], 0)

        s = "balloon"

        s_char_dict = {}
        for i in range(len(s)):
            s_char_dict[s[i]] = 1 + s_char_dict.get(s[i], 0)

        #Based on my failed intuition, my new intuition is to //(divide) the freq of text dict using char dict to handle the multiple repeating characters in "balloon"
        min_rep = float('inf')
        non_dup_s = set(s)

        for ch in non_dup_s:
            if ch in text_char_dict.keys():
                text_char_dict[ch] //= s_char_dict[ch]
                min_rep = min(min_rep, text_char_dict.get(ch, 0))
            else:
                return 0

        return min_rep

        

