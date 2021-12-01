from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1 = Counter(s1)
        w = Counter()
        need = n
        left = 0
        for right, c in enumerate(s2):
            w[c] += 1
            if w[c] <= s1[c]:
                need -= 1
                if need == 0:
                    return True
            else:
                while (lc := s2[left]) != c:
                    w[lc] -= 1
                    if w[lc] < s1[lc]:
                        need += 1
                    left += 1
                w[s2[left]] -= 1
                left += 1
        return False
