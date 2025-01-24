from functools import cache

# 官方题解方法一：记忆化搜索
# 时间复杂度O(n²)，空间复杂度O(n)
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        @cache
        def dp(index):
            """购买从下标index开始的所有水果需要花费的最少金币"""
            if 2 * index + 2 >= len(prices):
                return prices[index]
            return prices[index] + min(dp(i) for i in range(index + 1, 2 * index + 3))
        return dp(0)
