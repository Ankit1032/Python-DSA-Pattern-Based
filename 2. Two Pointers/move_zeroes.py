class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #My Solution
        # start = 0 #track zeroes
        # end = 1 #track non-zeroes

        # while start < len(nums) and end < len(nums):

        #     if nums[start] == 0 and nums[end] != 0: #swap when start is 0 and end is non zero
        #         nums[start], nums[end] = nums[end], nums[start]
        #         start += 1
        #         end += 1
            
        #     elif nums[start] != 0: #move start pointer until start reaches 0
        #         start += 1

        #         if end <= start:
        #             end += 1

        #     elif nums[end] == 0: #move end pointer until end reaches non zero
        #         end += 1

        #Better Solution - Neetcode, keep moving the non-zero elements to the left
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            


        
