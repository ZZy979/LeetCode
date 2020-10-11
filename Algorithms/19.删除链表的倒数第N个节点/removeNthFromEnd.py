# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        p = new_head
        length = 0
        while p.next:
            length += 1
            p = p.next
        p = new_head
        for i in range(length - n):
            p = p.next
        p.next = p.next.next
        return new_head.next
