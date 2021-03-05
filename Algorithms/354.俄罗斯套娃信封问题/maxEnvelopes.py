# 动态规划，时间复杂度O(n²)
# 9300 ms
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort()
        dp = [0] * len(envelopes)
        for i in range(len(envelopes)):
            dp[i] = max((dp[j] for j in range(i) if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]), default=0) + 1
        return max(dp)
