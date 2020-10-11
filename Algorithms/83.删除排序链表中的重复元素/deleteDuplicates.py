# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        x = None
        p = new_head
        while p.next is not None:
            if p.next.val == x:
                p.next = p.next.next
            else:
                x = p.next.val
                p = p.next
        return new_head.next
