# 官方题解：动态规划，记录转移过程
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [float('-inf')] * (target + 1)
        dp[0] = 0
        for c in cost:
            for j in range(c, target + 1):
                dp[j] = max(dp[j], dp[j - c] + 1)
        if dp[target] < 0:
            return '0'
        
        ans = []
        j = target
        for i in range(8, -1, -1):
            c = cost[i]
            while j >= c and dp[j] == dp[j - c] + 1:
                ans.append(str(i + 1))
                j -= c
        return ''.join(ans)
