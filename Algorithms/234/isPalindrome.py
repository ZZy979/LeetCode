# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 方法1：栈，时间复杂度O(n)，空间复杂度O(n)
# 692 ms
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        length = 0
        p = head
        while p:
            length += 1
            p = p.next

        stack = []
        p = head
        for i in range(length // 2):
            stack.append(p.val)
            p = p.next
        if length % 2 == 1:
            p = p.next
        while p:
            if stack[-1] != p.val:
                return False
            else:
                stack.pop()
                p = p.next
        return True
