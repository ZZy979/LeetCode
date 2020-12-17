# 官方题解：动态规划（考虑价格而不是差价）
# 时间复杂度O(n)，空间复杂度O(1)
# 728 ms
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        sell, buy = 0, -prices[0]
        for i in range(1, n):
            sell, buy = max(sell, buy + prices[i] - fee), max(buy, sell - prices[i])
        return sell
