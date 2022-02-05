class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        return next((s[i:i + n] for n in range(len(s), 1, -1) for i in range(len(s) + 1 - n) if is_nice_string(s[i:i + n])), '')


def is_nice_string(s):
    return len(set(s)) == len(set(s.lower())) * 2
