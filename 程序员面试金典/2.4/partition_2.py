# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 双指针+交换值
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        pre = cur = head
        while cur is not None:
            if cur.val < x:
                pre.val, cur.val = cur.val, pre.val
                pre = pre.next
            cur = cur.next
        return head
