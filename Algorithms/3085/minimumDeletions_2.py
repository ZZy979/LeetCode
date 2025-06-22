from collections import Counter

# 官方题解：散列表+枚举，时间复杂度O(n+C²)，空间复杂度O(C)，其中C=26
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        res = len(word)
        for a in cnt.values():
            deleted = 0
            for b in cnt.values():
                if b < a:
                    deleted += b
                elif b > a + k:
                    deleted += b - (a + k)
            res = min(res, deleted)
        return res
