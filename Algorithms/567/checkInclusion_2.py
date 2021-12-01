from collections import Counter

# 官方题解
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        s1_count = Counter(s1)
        win_count = Counter()
        match = 0
        left = 0
        for right, c in enumerate(s2):
            if s1_count[c] > 0:
                win_count[c] += 1
                if win_count[c] == s1_count[c]:
                    match += 1
            while match == len(s1_count):
                if right - left + 1 == len(s1):
                    return True
                lc = s2[left]
                if s1_count[lc] > 0:
                    win_count[lc] -= 1
                    if win_count[lc] < s1_count[lc]:
                        match -= 1
                left += 1
        return False
