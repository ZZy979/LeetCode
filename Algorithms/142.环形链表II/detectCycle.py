# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                break
        else:
            return None
        
        p = head
        while p is not slow:
            p = p.next
            slow = slow.next
        return p
