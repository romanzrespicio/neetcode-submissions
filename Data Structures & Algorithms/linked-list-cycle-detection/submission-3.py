# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dct = set()

        dummy = ListNode()
        dummy.next = head
        curr = dummy

        while curr:
            if curr in dct:
                return True
            dct.add(curr)
            curr = curr.next 
        
        return False