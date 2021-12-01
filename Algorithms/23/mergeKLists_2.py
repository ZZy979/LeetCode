# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

# 方法2：使用堆根据链表首元素排序
# 时间复杂度O((k+n)log k))，空间复杂度O(n)，n为元素总个数，k为链表个数
# 96 ms
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
