# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = p = ListNode(0)  # 头节点
        carry = 0
        while l1 and l2:
            x = l1.val + l2.val + carry
            p.next = ListNode(x % 10)
            carry = x // 10
            l1 = l1.next
            l2 = l2.next
            p = p.next
        while l1:
            x = l1.val + carry
            p.next = ListNode(x % 10)
            carry = x // 10
            l1 = l1.next
            p = p.next
        while l2:
            x = l2.val + carry
            p.next = ListNode(x % 10)
            carry = x // 10
            l2 = l2.next
            p = p.next
        if carry:
            p.next = ListNode(carry)
        return result.next
