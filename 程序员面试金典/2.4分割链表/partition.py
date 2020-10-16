# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 将小于x的节点移动到前面
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        p = new_head
        while p.next is not None:
            if p.next.val < x and p is not new_head:
                node = p.next
                p.next = node.next
                node.next = new_head.next
                new_head.next = node
            else:
                p = p.next
        return new_head.next
