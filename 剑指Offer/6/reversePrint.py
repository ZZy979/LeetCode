# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 方法1：递归，40 ms
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        reverse_rec(head, res)
        return res


def reverse_rec(head, res):
    if not head:
        return
    reverse_rec(head.next, res)
    res.append(head.val)
