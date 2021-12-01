# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 官方题解：模拟两个链表，40 ms
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_head = small = ListNode(0)
        large_head = large = ListNode(0)
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next
        large.next = None
        small.next = large_head.next
        return small_head.next
