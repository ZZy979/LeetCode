# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 移动节点，48 ms
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        new_head = ListNode(0)
        new_head.next = head
        prev = cur = new_head
        while cur.next:
            if cur.next.val < x:
                insert_after(prev, remove_next(cur))
                if cur is prev:
                    cur = cur.next
                prev = prev.next
            else:
                cur = cur.next
        return new_head.next


def remove_next(node):
    node_next = node.next
    node.next = node_next.next
    return node_next


def insert_after(prev, node):
    node.next = prev.next
    prev.next = node
