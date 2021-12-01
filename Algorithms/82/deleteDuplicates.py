# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        vhead = prev = ListNode(0, head)
        while prev.next:
            p = prev.next
            if p.next and p.next.val == p.val:
                while p and p.val == prev.next.val:
                    p = p.next
                prev.next = p
            else:
                prev = p
        return vhead.next
