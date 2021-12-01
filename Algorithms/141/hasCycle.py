# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 散列表（集合）法
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        seen = set()
        p = head
        while p is not None:
            if p in seen:
                return True
            else:
                seen.add(p)
            p = p.next
