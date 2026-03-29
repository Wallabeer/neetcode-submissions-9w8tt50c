class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = 0

        while left < right:
            volume = (right - left) * min(heights[left], heights[right])
            result = max(result, volume)

            if heights[left] < heights[right]:
                left = left + 1
            else:
                right = right -1
        
        return result