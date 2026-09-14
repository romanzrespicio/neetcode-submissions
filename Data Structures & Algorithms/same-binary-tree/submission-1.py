# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        check = True

        def dfs(p, q):
            nonlocal check

            if not p and not q:
                return
            elif not p or not q:
                check = False
                return

            dfs(p.left, q.left)
            dfs(p.right, q.right)

            if p.val != q.val:
                check = False
            
            return
        
        dfs(p, q)

        return check