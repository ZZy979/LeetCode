class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        ALICE, BOB = 0, 1
        # dp[p][i]: 轮到玩家p，该拿第i堆石子，Alice的最高得分
        dp = [[0] * (n + 1) for _ in range(2)]
        for i in range(n - 1, -1, -1):
            dp[ALICE][i] = max(sum(stoneValue[i:i + m]) + dp[BOB][i + m] for m in range(1, min(n - i, 3) + 1))
            dp[BOB][i] = min(dp[ALICE][i + m] for m in range(1, min(n - i, 3) + 1))
        return 'Alice' if dp[ALICE][0] > dp[BOB][0] else 'Bob' if dp[ALICE][0] < dp[BOB][0] else 'Tie'
