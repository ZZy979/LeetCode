class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = 99999999, 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit
