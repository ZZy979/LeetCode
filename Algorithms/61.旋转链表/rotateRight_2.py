# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 官方题解：闭合成环
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head
        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        k %= n
        if k == 0:
            return head
        
        cur.next = head
        for _ in range(n - k):
            cur = cur.next
        ret = cur.next
        cur.next = None
        return ret
