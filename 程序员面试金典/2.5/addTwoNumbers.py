# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = p = ListNode(0)  # 头节点
        carry = 0
        while l1 or l2:
            x = 0 if l1 is None else l1.val
            y = 0 if l2 is None else l2.val
            s = x + y + carry
            p.next = ListNode(s % 10)
            carry = s // 10
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
            p = p.next
        if carry:
            p.next = ListNode(carry)
        return result.next
