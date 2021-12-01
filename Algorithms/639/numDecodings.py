# 官方题解：动态规划
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        a, b, c = 0, 1, 0  # f[i-2], f[i-1], f[i]
        r = 10**9 + 7
        for i in range(1, n + 1):
            c = alpha(s[i - 1]) * b
            if i > 1:
                c += beta(s[i - 2], s[i - 1]) * a
            c %= r
            a, b = b, c
        return c

def alpha(c):
    return 9 if c == '*' else 0 if c == '0' else 1

def beta(c1, c2):
    if c1 == '*':
        return 15 if c2 == '*' else 2 if '0' <= c2 <= '6' else 1
    elif c1 == '0' or '3' <= c1 <= '9':
        return 0
    elif c1 == '1':
        return 9 if c2 == '*' else 1
    else:
        return 6 if c2 == '*' else 1 if '0' <= c2 <= '6' else 0
