from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}
        dp = defaultdict(lambda: 2)
        ans = 0
        for k in range(len(arr)):
            for j in range(k):
                if (i := index.get(arr[k] - arr[j])) is not None and i < j:
                    dp[j, k] = dp[i, j] + 1
                    ans = max(ans, dp[j, k])
        return ans if ans >= 3 else 0
