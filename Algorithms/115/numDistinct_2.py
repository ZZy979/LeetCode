class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(t)
        pre = [0] * (n + 1)
        pre[0] = 1
        for c in s:
            for i in reversed(range(n)):
                if c == t[i]:
                    pre[i + 1] += pre[i]
        return pre[-1]
