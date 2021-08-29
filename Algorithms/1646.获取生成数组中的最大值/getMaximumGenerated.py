class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        a = [0] * (n + 1)
        a[1] = 1
        for i in range(2, n + 1):
            a[i] = a[i // 2] if i % 2 == 0 else a[i // 2] + a[i // 2 + 1]
        return max(a)
