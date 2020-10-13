# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 迭代版本
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = head
        new_head = head.next
        while p and p.next:
            q = p.next
            p.next = q.next
            q.next = p
            p_next = p.next
            if p.next and p.next.next:
                p.next = p.next.next
            p = p_next
        return new_head
