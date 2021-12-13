# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for i, p in enumerate(lists):
            if p:
                heapq.heappush(heap, (p.val, i, p))
        head = q = ListNode(0)
        while heap:
            v, i, p = heapq.heappop(heap)
            q.next = ListNode(v)
            q = q.next
            if p.next:
                heapq.heappush(heap, (p.next.val, i, p.next))
        return head.next
