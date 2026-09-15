# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        ll_1 = head
        ll_2 = prev
        while ll_1 and ll_2:
            nxt_1 = ll_1.next
            nxt_2 = ll_2.next
            ll_1.next = ll_2
            ll_2.next = nxt_1
            ll_1 = nxt_1
            ll_2 = nxt_2
        
        return


