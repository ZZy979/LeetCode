# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random

# 官方题解：蓄水池算法
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        p, i, res = self.head, 1, 0
        while p:
            if random.randrange(i) == 0:  # P=1/i
                res = p.val
            i += 1
            p = p.next
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
