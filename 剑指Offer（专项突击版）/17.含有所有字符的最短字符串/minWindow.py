from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = Counter(t)
        w = Counter()
        start, min_len = 0, 100001
        left = right = 0
        match = 0
        for right, c in enumerate(s):
            if t[c] > 0:
                w[c] += 1
                if w[c] == t[c]:
                    match += 1
            while match == len(t):
                if right - left + 1 < min_len:
                    start, min_len = left, right - left + 1
                lc = s[left]
                if t[lc] > 0:
                    w[lc] -= 1
                    if w[lc] < t[lc]:
                        match -= 1
                left += 1
        return '' if min_len > len(s) else s[start:start + min_len]
