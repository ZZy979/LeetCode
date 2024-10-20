# 动态规划
class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            # 第一枚鸡蛋从k楼扔下，如果碎了则还需要k-1次操作，否则还需要dp[i-k]次操作
            dp[i] = min(max(k - 1, dp[i - k]) + 1 for k in range(1, i))
        return dp[n]
