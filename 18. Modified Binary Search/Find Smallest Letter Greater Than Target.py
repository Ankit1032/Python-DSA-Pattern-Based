class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        '''
        Explanation:
        We use binary search and keep updating the result whenever we find a character greater than target and then we move left
        if current character is lesser than target then move right and no need to store that current element to result as questions asks us to store letters which is lexographically closer and greater than target
        '''

        result = letters[0] #we keeps letters[0] because if there's no character greater than target, then return the smallest character, stated by the question itself 

        left = 0
        right = len(letters) - 1

        while left <= right:

            mid = (left+right)//2

            if letters[mid] > target:
                result = letters[mid]
                right = mid - 1
            else:
                left = mid + 1
        
        return result
