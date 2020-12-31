# 官方题解2：贪心算法（类似于452题）
# 时间复杂度O(nlog n)，空间复杂度O(log n)（排序所需的栈空间）
# 96 ms
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        right = intervals[0][1]
        ans = 1
        for i in range(1, n):
            if intervals[i][0] >= right:
                ans += 1
                right = intervals[i][1]
        return n - ans
