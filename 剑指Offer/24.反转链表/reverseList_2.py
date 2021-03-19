# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        head, tail = reverse(head)
        tail.next = None
        return head
    

def reverse(head):
    if not head.next:
        return head, head
    new_head, tail = reverse(head.next)
    tail.next = head
    return new_head, head
