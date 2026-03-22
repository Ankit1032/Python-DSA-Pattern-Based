class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        max_sub_array_len = 0
        left = 0
        flips = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                flips += 1

            while flips > k:
                if nums[left] == 0:
                    flips -= 1
                left += 1

            if (nums[right] == 1) or (nums[right] == 0 and flips <= k):
                window_len = right - left + 1
                max_sub_array_len = max(max_sub_array_len, window_len)

        
        return max_sub_array_len
