class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        #cyclic sort

        i = 0
        while i < len(nums):

            correct = nums[i] - 1

            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        
        print(nums)
            
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return nums[i]
        
