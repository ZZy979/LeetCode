# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 向前移动奇数节点
# 52 ms
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        odd, even = head, head.next
        while even and even.next:
            insert_after(odd, remove_next(even))
            odd = odd.next
            even = even.next
        return head


def remove_next(node):
    next = node.next
    node.next = next.next
    return next


def insert_after(prev, node):
    node.next = prev.next
    prev.next = node
