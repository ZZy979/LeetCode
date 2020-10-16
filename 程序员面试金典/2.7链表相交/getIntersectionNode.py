# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        length_a = 0
        p = headA
        while p:
            length_a += 1
            p = p.next

        length_b = 0
        q = headB
        while q:
            length_b += 1
            q = q.next

        if p is not q:
            return None

        p = headA
        q = headB
        if length_a > length_b:
            for i in range(length_a - length_b):
                p = p.next
        elif length_a < length_b:
            for i in range(length_b - length_a):
                q = q.next
        while p is not q:
            p = p.next
            q = q.next
        return p
