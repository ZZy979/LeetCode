# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p, prev = head, None
        while p:
            p.next, prev, p = prev, p, p.next
        return prev
