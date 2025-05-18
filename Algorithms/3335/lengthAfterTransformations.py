# 动态规划，时间复杂度O(Ct+n)，空间复杂度O(C)，其中C=26
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        q = 10**9 + 7
        dp = [1] * 26
        for i in range(1, t + 1):
            dp_new = [0] * 26
            dp_new[25] = (dp[0] + dp[1]) % q
            for j in range(24, -1, -1):
                dp_new[j] = dp[j + 1]
            dp = dp_new
        return sum(dp[ord(c) - ord('a')] for c in s) % q
