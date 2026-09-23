# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        val = 0

        def dfs(root, truthy):
            
            nonlocal res
            nonlocal val

            if not root:
                return 
            
            if truthy == True:
                return 

            dfs(root.left, truthy)
            val += 1

            if val == k:
                truthy = True
                res = root.val

            dfs(root.right, truthy)

            return

        dfs(root, False)

        return res

            