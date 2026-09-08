"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        dct = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            dct[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = dct[curr]
            copy.next = dct[curr.next]
            copy.random = dct[curr.random]
            curr = curr.next
        
        return dct[head]

