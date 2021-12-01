# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        vhead = pre = ListNode(-1, head)
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        # 每次把cur后的节点插入pre之后
        for _ in range(right - left):
            nex = cur.next
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
        return vhead.next
