class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 0x7fffffff
        profit = 0
        for p in prices:
            min_price = min(min_price, p)
            profit = max(profit, p - min_price)
        return profit
