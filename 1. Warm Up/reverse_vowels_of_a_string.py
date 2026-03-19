class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s_list = list(s)
        start = 0
        end = len(s_list)-1

        while start < end:
            if s_list[start] in vowels and s_list[end] in vowels:
                temp = s_list[start]
                s_list[start] = s_list[end]
                s_list[end] = temp
                start += 1 # I forgot to add these pointers in the initial run, my bad
                end -= 1

            if s_list[start] not in vowels:
                start += 1
            
            if s_list[end] not in vowels:
                end -= 1

        return "".join(s_list)
