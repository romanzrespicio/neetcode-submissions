class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = 0

        while i < j:
            length = j - i
            height = min(heights[i], heights[j])
            curr_area = length * height
            max_area = max(max_area, curr_area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return max_area