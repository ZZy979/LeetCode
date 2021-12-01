import operator

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for m in range(1, n + 1, 2):
            p = min(m, n - m + 1)
            weight = [p] * n
            weight[:p] = range(1, p + 1)
            weight[-p:] = range(p, 0, -1)
            ans += sum(map(operator.mul, weight, arr))
        return ans
