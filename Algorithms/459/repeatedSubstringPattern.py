class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                for k in range(i, n, i):
                    if s[k:k + i] != s[:i]:
                        break
                else:
                    return True
        return False
