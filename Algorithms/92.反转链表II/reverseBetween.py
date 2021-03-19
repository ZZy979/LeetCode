# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        vhead = p = ListNode(0, head)
        for _ in range(left - 1):
            p = p.next
        node_before_left = p
        node_left = p = p.next
        prev = None
        for _ in range(right - left + 1):
            prev, prev.next, p = p, prev, p.next
        node_before_left.next = prev
        node_left.next = p
        return vhead.next
