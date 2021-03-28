# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        length = list_length(head)
        k %= length
        if k == 0:
            return head

        p = head
        for _ in range(length - k - 1):
            p = p.next
        new_head, p.next = p.next, None

        p = new_head
        while p.next:
            p = p.next
        p.next = head
        return new_head


def list_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length
