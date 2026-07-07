class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0
        i = 0
        j = len(heights) - 1
        area_i = 0
        area_j = 0

        while i < j:
            
            length = (j - i)
            area = length * min(heights[i], heights[j])
            print(length)
            max_area = max(max_area, area)
            print(max_area)
            
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return max_area