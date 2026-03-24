class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # Two pointer solution
        # left = 0
        # right = len(s) - 1

        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1
        
        #Stack solution (Do not use this as question asks u to achieve in O(1) memory)
        s1 = s.copy()
        rev_list = []

        while s1 != []:
            rev_list.append(s1[-1])
            s1.pop()
        
        # modify original list in-place
        for i in range(len(s)):
            s[i] = rev_list[i]


        
        

