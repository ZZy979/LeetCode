# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

# 方法1：将所有元素放入堆中
# 时间复杂度O(nlog n)，空间复杂度O(n)，n为元素总个数
# 104 ms
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for p in lists:
            while p:
                heapq.heappush(heap, p.val)
                p = p.next
        head = p = ListNode(0)
        while heap:
            p.next = ListNode(heapq.heappop(heap))
            p = p.next
        return head.next
