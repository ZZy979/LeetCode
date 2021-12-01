# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 递归版本
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        length = self.length_of_list(head)
        return self.is_palindrome_rec(head, length)[1]

    def length_of_list(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def is_palindrome_rec(self, head, length):
        if not head or length <= 0:
            return head, True
        elif length == 1:
            return head.next, True
        node, res = self.is_palindrome_rec(head.next, length - 2);
        if not res or not node:
            return node, res
        return node.next, head.val == node.val
