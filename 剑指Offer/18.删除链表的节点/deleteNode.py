# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        vhead = p = ListNode(0)
        vhead.next = head
        while p.next and p.next.val != val:
            p = p.next
        if p.next:
            p.next = p.next.next
        return vhead.next
