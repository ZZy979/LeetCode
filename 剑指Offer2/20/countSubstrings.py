class Solution:
    def countSubstrings(self, s: str) -> int:
        return sum(count(s, i, i) + count(s, i, i + 1) for i in range(len(s)))


def count(s, start, end):
    res = 0
    while start >= 0 and end < len(s) and s[start] == s[end]:
        res += 1
        start -= 1
        end += 1
    return res
