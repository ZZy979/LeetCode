class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m, n = len(values), len(values[0])
        next_buy = [n - 1] * m
        ans = 0
        for d in range(1, m * n + 1):
            next_values = [values[i][next_buy[i]] if next_buy[i] >= 0 else 0xFFFFFFFF for i in range(m)]
            v = min(next_values)
            j = next_values.index(v)
            ans += v * d
            next_buy[j] -= 1
        return ans
