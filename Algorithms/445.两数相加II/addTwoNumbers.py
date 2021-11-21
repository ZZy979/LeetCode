# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 方法1：反转链表
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return reverse(add(reverse(l1), reverse(l2)))


def reverse(head):
    p, prev = head, None
    while p:
        p.next, prev, p = prev, p, p.next
    return prev


def add(l1, l2):
    result = p = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        x = y = 0
        if l1:
            x, l1 = l1.val, l1.next
        if l2:
            y, l2 = l2.val, l2.next
        carry, val = divmod(x + y + carry, 10)
        p.next = ListNode(val)
        p = p.next
    return result.next
