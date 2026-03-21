class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #My solution - applying two sum twice as there are 3 balls
        left = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                nums[left], nums[right]  = nums[right], nums[left]
                left += 1
                right += 1
        
        for right in range(len(nums)):
            if nums[right] == 1:
                nums[left], nums[right]  = nums[right], nums[left]
                left += 1
                right += 1
        

            
        
