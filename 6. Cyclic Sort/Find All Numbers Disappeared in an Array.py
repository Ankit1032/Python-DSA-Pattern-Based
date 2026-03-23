class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        #cyclic sort
        i = 0
        result = []
        while i < len(nums):

            correct = nums[i] - 1

            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
            

        for i in range(len(nums)):
            if i != nums[i]-1:
                result.append(i+1)

        return result
