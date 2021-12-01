# 官方题解1：动态规划
# 时间复杂度O(n²)，空间复杂度O(n²)
# 9464 ms
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ''
        # 枚举子串长度
        for r in range(n):
            for i in range(n - r):
                j = i + r
                if r == 0:
                    dp[i][i] = True
                elif r == 1:
                    dp[i][i + 1] = s[i] == s[i + 1]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j] and r + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans
