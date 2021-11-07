class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for x in arr:
            dp[x] = dp.get(x - difference, 0) + 1
        return max(dp.values())
