# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # pass left and at each node, check left, right and node and see if equal to subroot
        
        def sameTree(p, q):
            if not p and not q:
                return True
            
            if p and q and (p.val == q.val):
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)

            else:
                return False

        def dfs(root, subRoot):
            if not root:
                return False

            return dfs(root.left, subRoot) or dfs(root.right, subRoot) or sameTree(root, subRoot)

        return dfs(root, subRoot)