import bisect

# 官方题解：动态规划+二分查找，时间复杂度O(nk+nlog n)，空间复杂度O(nk)
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda e: e[1])
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n + 1)]  # dp[i][j]表示前i个会议中最多参加j个会议的最大价值和
        for i, (start, end, val) in enumerate(events):
            p = bisect.bisect_left(events, start, hi=n - 1, key=lambda e: e[1])
            for j in range(1, k + 1):
                dp[i + 1][j] = max(dp[i][j], dp[p][j - 1] + events[i][2])
        return dp[n][k]
