# 官方题解1：动态规划
# f[i]: 区间0~i中互不重叠的最大区间数量
# 时间复杂度O(n²)，空间复杂度O(n)
# 6920 ms
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        n = len(intervals)
        f = [1]
        for i in range(1, n):
            f.append(max((f[j] for j in range(i) if intervals[j][1] <= intervals[i][0]), default=0) + 1)
        return n - max(f)
