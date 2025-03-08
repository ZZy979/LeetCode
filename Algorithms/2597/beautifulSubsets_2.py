from collections import defaultdict, Counter

# 官方题解：动态规划，时间复杂度O(nlog n)，空间复杂度O(n)
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        groups = defaultdict(Counter)
        for x in nums:
            groups[x % k][x] += 1
        
        ans = 1
        for g in groups.values():
            arr = sorted(g)
            m = len(arr)
            f = [[0] * 2 for _ in range(m)]
            f[0][0] = 1
            f[0][1] = 2**g[arr[0]] - 1
            for i in range(1, m):
                f[i][0] = f[i - 1][0] + f[i - 1][1]
                if arr[i] - arr[i - 1] == k:
                    f[i][1] = f[i - 1][0] * (2**g[arr[i]] - 1)
                else:
                    f[i][1] = (f[i - 1][0] + f[i - 1][1]) * (2**g[arr[i]] - 1)
            ans *= f[m - 1][0] + f[m - 1][1]
        return ans - 1
