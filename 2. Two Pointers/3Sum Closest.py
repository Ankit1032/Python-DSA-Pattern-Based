import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        closest_result = math.inf
        nums.sort()

        for index, value in enumerate(nums):
            
            left = index+1
            right = len(nums)-1

            while left < right:
                result = value + nums[left] + nums[right]

                if abs(target - result) < abs(closest_result - target): #tracking the closest result else following 3sum pattern
                    closest_result = result

                if result > target:
                    right -= 1
                else:
                    left += 1
        
        return closest_result


