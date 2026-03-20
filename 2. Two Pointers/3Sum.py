class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        # Idea is to use one pointer iterating from start to end and for remaining 2 pointers, we will use the same logic used in Two Sum II - Input Array Is Sorted

        three_pairs = []
        nums.sort() #the two sum logic only works on sorted array

        for index,i in enumerate(nums):
            if index > 0 and i == nums[index - 1]: #the array contains duplicate numbers and we Because we don't want duplicates in our pairs mentioned in the quesion
                continue

            left = index+1
            right = len(nums) - 1

            while left < right:
                
                result = i + nums[left] + nums[right]
                if result == 0:
                    three_pairs.append([i,nums[left],nums[right]])
                    left += 1
                    right -= 1

                    # if we had [-2,-2,0,0,2,2] -> we will have to handle duplicates in 2 sum case as well
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif result > 0:
                    right -= 1
                else:
                    left += 1

        return three_pairs
                
                
