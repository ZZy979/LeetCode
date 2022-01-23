class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp0, dp1, dp2 = 0, 0, 0
        s = 0
        for i in range(n - 1, -1, -1):
            s += stoneValue[i]
            dp0, dp1, dp2 = s - min(dp0, dp1, dp2), dp0, dp1
        res = dp0 * 2 - s
        return 'Tie' if res == 0 else 'Alice' if res > 0 else 'Bob'
