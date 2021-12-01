# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 方法2：栈，52 ms
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        p = head
        while p:
            stack.append(p.val)
            p = p.next
        return list(reversed(stack))
