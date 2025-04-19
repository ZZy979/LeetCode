# 官方题解：前缀和，时间复杂度O(n²+nM)，空间复杂度O(M)，其中M=max(arr)
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        n, mx = len(arr), max(arr)
        total = [0] * (mx + 1)  # total[i]为arr中[0, i]之间的值出现次数的总和
        for j in range(n - 1):
            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) <= b:
                    l = max(0, arr[j] - a, arr[k] - c)
                    r = min(mx, arr[j] + a, arr[k] + c)
                    if l <= r:
                        ans += total[r] if l == 0 else total[r] - total[l - 1]
            for v in range(arr[j], mx + 1):
                total[v] += 1
        return ans
