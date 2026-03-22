class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        window_sum = 0
        min_subarray = float('inf')

        l = 0
        for r in range(len(nums)):
            window_sum += nums[r]
            
            while window_sum >= target:
                window_len = r - l + 1
                min_subarray = min(min_subarray, window_len)
                window_sum -= nums[l]
                l+=1              

        if min_subarray == float('inf'):
            return 0
            
        return min_subarray
            
            
