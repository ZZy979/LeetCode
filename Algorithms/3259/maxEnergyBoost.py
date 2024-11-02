class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [energyDrinkA[0], energyDrinkB[0]]
        dp[1] = [energyDrinkA[0] + energyDrinkA[1], energyDrinkB[0] + energyDrinkB[1]]
        for i in range(2, n):
            dp[i] = [
                max(dp[i - 1][0], dp[i - 2][1]) + energyDrinkA[i],
                max(dp[i - 1][1], dp[i - 2][0]) + energyDrinkB[i]
            ]
        print(dp)
        return max(dp[-1][0], dp[-1][1])
