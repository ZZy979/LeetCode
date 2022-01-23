class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        q = 10**9 + 7
        for _ in range(n - 1):
            a, e, i, o, u = (e + i + u) % q, (a + i) % q, (e + o) % q, i, (i + o) % q
        return (a + e + i + o + u) % q
