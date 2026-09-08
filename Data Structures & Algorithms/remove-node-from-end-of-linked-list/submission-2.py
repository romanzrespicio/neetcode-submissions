# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = dummy = ListNode()
        curr.next = head
        len_ll = 0
        
        while curr:
            len_ll += 1
            curr = curr.next
        
        remove_idx = len_ll - n
        idx = 0
        tmp = None
        curr = dummy
        prev = ListNode()

        while curr and (idx != remove_idx):
            prev = curr
            curr = curr.next
            tmp = curr.next
            idx += 1

        prev.next = tmp
        head = dummy.next

        return head


