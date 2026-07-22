class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        out = 0
        rightMax = [0] * len(height)
        leftMax = [0] * len(height)

        leftMax[0] = height[0]
        for i in range(1, len(height)):
            leftMax[i] = max(height[i], leftMax[i-1])

        rightMax[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i+1])

        for i in range(len(height)):
            out += min(leftMax[i], rightMax[i]) - height[i]

        return out
