# 动态规划
# 时间复杂度O(n)，空间复杂度O(n)
# 1076 ms
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        own = [0] * n  # 前i天，最后持有
        not_own = [0] * n  # 前i天，最后不持有
        own[0] = -fee
        for i in range(1, n):
            own[i] = max(own[i - 1] + prices[i] - prices[i - 1], not_own[i - 1] - fee)
            not_own[i] = max(own[i - 1] + prices[i] - prices[i - 1], not_own[i - 1])
        return not_own[-1]
