# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = prev = ListNode(0, head)
        while head:
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = reverse_list(head, tail)
            prev.next = head
            head = tail.next = nex
            prev = tail
        return hair.next


def reverse_list(head, tail):
    p, prev = head, tail.next
    while prev is not tail:
        nex = p.next
        p.next = prev
        prev = p
        p = nex
    return tail, head
