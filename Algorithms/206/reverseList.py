# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        else:
            new_head, tail = self.reverseListRec(head)
            tail.next = None
            return new_head
    
    def reverseListRec(self, node):
        if node.next is None:
            return node, node
        else:
            head, tail = self.reverseListRec(node.next)
            tail.next = node
            return head, node
