# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        seen = set()
        new_head = ListNode(0)
        new_head.next = head
        p = new_head
        while p.next is not None:
            if p.next.val in seen:
                p.next = p.next.next
            else:
                seen.add(p.next.val)
                p = p.next
        return new_head.next
