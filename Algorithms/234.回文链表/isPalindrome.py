# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        new_head = ListNode(0)
        new_head.next = head

        length = 0
        p = new_head
        while p.next is not None:
            length += 1
            p = p.next

        stack = []
        p = new_head
        for i in range(length // 2):
            stack.append(p.next.val)
            p = p.next
        if length % 2 == 1:
            p = p.next
        while p.next is not None:
            if stack[-1] != p.next.val:
                return False
            else:
                stack.pop()
                p = p.next
        return True
