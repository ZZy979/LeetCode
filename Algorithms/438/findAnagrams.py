from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = n = len(p)
        p = Counter(p)
        w = Counter()
        left = 0
        ans = []
        for right, c in enumerate(s):
            w[c] += 1
            if w[c] <= p[c]:
                need -= 1
            else:
                while (lc := s[left]) != c:
                    w[lc] -= 1
                    if w[lc] < p[lc]:
                        need += 1
                    left += 1
                w[s[left]] -= 1
                left += 1
            if need == 0:
                ans.append(left)
        return ans
