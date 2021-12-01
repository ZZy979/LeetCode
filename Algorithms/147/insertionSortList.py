# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = ListNode(0)
        new_head.next = head
        p = new_head.next
        while p.next:
            q = new_head
            while q.next.val < p.next.val:
                q = q.next
            insert_after(q, remove_next(p))
            if q is p:
                p = p.next
        return new_head.next


def remove_next(node):
    node_next = node.next
    node.next = node_next.next
    return node_next


def insert_after(prev, node):
    node.next = prev.next
    prev.next = node
