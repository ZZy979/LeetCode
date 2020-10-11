class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        a = [True] * n
        a[0] = a[1] = False
        for i in range(2, n):
            if a[i]:
                for j in range(2 * i, n, i):
                    a[j] = False
        return sum(a)
