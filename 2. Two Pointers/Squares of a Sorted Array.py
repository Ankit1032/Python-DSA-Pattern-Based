class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        new_nums = []

        left = 0
        right = len(nums) - 1

        while left <= right:

            left_sq = nums[left]*nums[left]
            right_sq = nums[right]*nums[right]

            if left_sq > right_sq:
                new_nums.append(left_sq)
                left += 1
            else:
                new_nums.append(right_sq)
                right -= 1

        return new_nums[::-1]
