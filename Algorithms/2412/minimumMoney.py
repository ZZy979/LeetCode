class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        total_lose = mx = 0
        for cost, cashback in transactions:
            total_lose += max(cost - cashback, 0)
            mx = max(mx, min(cost, cashback))
        return total_lose + mx
