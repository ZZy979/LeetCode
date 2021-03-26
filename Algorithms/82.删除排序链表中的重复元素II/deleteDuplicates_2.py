# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = head.next
        if p.val == head.val:
            while p and p.val == head.val:
                p = p.next
            head = self.deleteDuplicates(p)
        else:
            head.next = self.deleteDuplicates(p)
        return head
