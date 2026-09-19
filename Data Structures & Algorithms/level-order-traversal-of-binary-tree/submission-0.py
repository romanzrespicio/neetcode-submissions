# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        def bfs(root):
            queue = collections.deque()

            if root:
                queue.append(root)

            print(queue)

            while len(queue) > 0:
                level = []

                for i in range(len(queue)):
                    curr = queue.popleft()
                    level.append(curr.val)

                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                       
                res.append(level)
                
            return
        
        bfs(root)

        return res
                    
                