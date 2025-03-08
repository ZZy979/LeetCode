import bisect

# 排序+二分查找，时间复杂度O(nlog n+qlog n)，空间复杂度O(log n)
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i - 1][1])
        answer = []
        for query in queries:
            i = bisect.bisect_right(items, query, key=lambda x: x[0])
            answer.append(0 if i == 0 else items[i - 1][1])
        return answer
