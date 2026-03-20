class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1

        max_area = -1

        while left < right:

            area = (right - left) * (min(height[left], height[right]))
            max_area = max(max_area, area)
            
            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                right -= 1
                left += 1

        return max_area

