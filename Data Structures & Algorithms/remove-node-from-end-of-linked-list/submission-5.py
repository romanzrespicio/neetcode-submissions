# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = dummy = ListNode()
        dummy.next = head
        
        while curr and n > 0:
            curr = curr.next
            n -= 1
        
        curr_2 = dummy
        prev = dummy
        
        while curr:
            curr = curr.next
            prev = curr_2
            curr_2 = curr_2.next
        
        
        prev.next = curr_2.next

        return dummy.next