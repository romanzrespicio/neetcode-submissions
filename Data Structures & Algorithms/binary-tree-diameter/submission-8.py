# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:    
        res = 0

        def dfs(root):
            nonlocal res 

            if not root:
                return -1

            maxDepthLeft = dfs(root.left) + 1
            maxDepthRight = dfs(root.right) + 1
            path = maxDepthLeft + maxDepthRight
            
            res = max(res, path)

            return max(maxDepthLeft, maxDepthRight)

        dfs(root)

        return res