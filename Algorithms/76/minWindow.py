from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = len(t)
        t = Counter(t)
        left = 0
        ans = (0, 100001)
        for right, c in enumerate(s):
            if t[c] > 0:
                need -= 1
            t[c] -= 1
            if need == 0:
                while t[s[left]] != 0:
                    t[s[left]] += 1
                    left += 1
                if right - left < ans[1] - ans[0]:
                    ans = (left, right)
                t[s[left]] += 1
                need += 1
                left += 1
        return '' if ans[1] >= len(s) else s[ans[0]:ans[1] + 1]
