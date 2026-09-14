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
                return 0

            maxDepthLeft = dfs(root.left) + 1
            maxDepthRight = dfs(root.right) + 1
            longestPathNode = dfs(root.left) + dfs(root.right)
            print(f"node: {root.val}")
            print(longestPathNode)
            res = max(res, longestPathNode)

            return max(maxDepthLeft, maxDepthRight)
        dfs(root)
        return res
