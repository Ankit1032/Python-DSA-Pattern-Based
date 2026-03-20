class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        #non-inplace solution
        # v = len(set(nums))
        # nums[:] = set(nums)

        # return v

        # Following move zeroes leetcode soltuion pattern 
        left = 0
        
        for right in range(left+1,len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
                

        return left+1
