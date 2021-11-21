# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 方法2：转换为数字
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return num2list(list2num(l1) + list2num(l2))


def list2num(head):
    res = 0
    while head:
        res = 10 * res + head.val
        head = head.next
    return res


def num2list(num):
    res = ListNode(0)
    while num:
        res.next = ListNode(num % 10, res.next)
        num //= 10
    return res.next or res
