from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        m, n = len(p), len(s)
        cs, cp = [0] * 26, [0] * 26
        ans = []
        for i in range(m):
            cs[ord(s[i]) - ord('a')] += 1
            cp[ord(p[i]) - ord('a')] += 1
        if cs == cp:
            ans.append(0)
        for i in range(m, n):
            cs[ord(s[i]) - ord('a')] += 1
            cs[ord(s[i - m]) - ord('a')] -= 1
            if cs == cp:
                ans.append(i - m + 1)
        return ans
