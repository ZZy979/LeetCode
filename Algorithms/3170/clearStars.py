from collections import defaultdict
from sortedcontainers import SortedSet

# 有序集合+二分查找，时间复杂度O(Cnlog n)，空间复杂度O(n)，其中C=26
class Solution:
    def clearStars(self, s: str) -> str:
        char_idx = defaultdict(SortedSet)
        for i, c in enumerate(s):
            char_idx[c].add(i)

        s = list(s)
        for star_idx in char_idx['*']:
            cur = 'a'
            while cur < 'z' and (not char_idx[cur] or star_idx < char_idx[cur][0]):
                cur = chr(ord(cur) + 1)
            i = char_idx[cur].bisect_left(star_idx)
            s[char_idx[cur].pop(i - 1)] = '.'
            s[star_idx] = '.'
        return ''.join(c for c in s if c != '.')
