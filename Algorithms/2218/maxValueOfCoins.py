# 官方题解：转化为背包问题
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        f = [0] + [-1] * k  # f[i]表示进行i次操作可以得到的最大面值之和
        for pile in piles:
            for i in range(k, 0, -1):
                value = 0
                for t in range(1, len(pile) + 1):
                    value += pile[t - 1]
                    if i >= t and f[i - t] != -1:
                        f[i] = max(f[i], f[i - t] + value)
        return f[k]
