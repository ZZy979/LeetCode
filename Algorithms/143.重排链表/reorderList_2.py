# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 栈，时间复杂度O(n)，空间复杂度O(n)
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next if fast.next else slow
        
        stack = []
        p = head
        while p is not slow:
            stack.append(p)
            p = p.next
        
        while stack:
            p = stack.pop()
            node = mid.next
            mid.next = node.next
            node.next = p.next
            p.next = node
