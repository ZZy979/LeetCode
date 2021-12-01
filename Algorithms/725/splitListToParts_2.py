# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        q, r = divmod(n, k)

        ans = [None] * k
        p = head
        for i in range(k):
            if not p:
                break
            ans[i] = p
            m = q + 1 if i < r else q
            for _ in range(m - 1):
                p = p.next
            next_, p.next = p.next, None
            p = next_
        return ans
