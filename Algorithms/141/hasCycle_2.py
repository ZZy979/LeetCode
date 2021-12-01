# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 双指针法
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False
