# 官方题解
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        s = [int(d) for d in str(N)]
        i = 1
        while i < len(s) and s[i] >= s[i - 1]:
            i += 1
        if i < len(s):
            while i > 0 and s[i] < s[i - 1]:
                s[i - 1] -= 1
                i -= 1
            for j in range(i + 1, len(s)):
                s[j] = 9
        return int(''.join(str(d) for d in s))
