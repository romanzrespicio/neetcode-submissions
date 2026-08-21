class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for idx, h in enumerate(heights):
            start = idx

            while stack and stack[-1][1] > h:
                sIdx, sH = stack.pop()
                maxArea = max(maxArea, sH * (idx - sIdx))
                start = sIdx
            
            stack.append((start, h))

        while stack:
            sIdx, sH = stack.pop()
            maxArea = max(maxArea, sH * (len(heights) - sIdx))
        
        return maxArea