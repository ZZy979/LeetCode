# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 方法2：找中点+反转链表，时间复杂度O(n)，空间复杂度O(1)
# 592 ms
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        mid = find_mid(head)
        tail = reverse(mid.next)
        p, q = head, tail
        while q:
            if p.val != q.val:
                return False
            p, q = p.next, q.next
        return True


def find_mid(head):
    fast = slow = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def reverse(head):
    p, prev = head, None
    while p:
        prev, prev.next, p = p, prev, p.next
    return prev
