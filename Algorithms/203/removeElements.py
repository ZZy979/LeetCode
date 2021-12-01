# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        p = new_head
        while p.next is not None:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return new_head.next
