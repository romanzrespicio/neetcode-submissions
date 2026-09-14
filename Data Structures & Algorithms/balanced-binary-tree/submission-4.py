# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        check = True

        def dfs(root):
            nonlocal check

            if not root:
                return 0
            
            maxDepthLeft = dfs(root.left) + 1
            maxDepthRight = dfs(root.right) + 1
            
            if abs(maxDepthLeft - maxDepthRight) > 1:
                check = False

            pass_val = max(maxDepthLeft, maxDepthRight)
            return pass_val

        dfs(root)
        
        return check