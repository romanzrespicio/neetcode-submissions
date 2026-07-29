class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax = height[0], height[-1]
        left, right = 0, len(height) - 1
        total = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(height[left], leftMax)
                total += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(height[right], rightMax)
                total += rightMax - height[right]
            
        return total