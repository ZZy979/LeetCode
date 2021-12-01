# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 递归，时间复杂度O(n)，空间复杂度O(n)
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next if fast.next else slow
        self.reorder_rec(mid, head, slow)
    
    def reorder_rec(self, mid, p, p_end):
        if p is p_end:
            return
        self.reorder_rec(mid, p.next, p_end)
        # 将mid的下一个节点移至p之后
        node = mid.next
        mid.next = node.next
        node.next = p.next
        p.next = node
