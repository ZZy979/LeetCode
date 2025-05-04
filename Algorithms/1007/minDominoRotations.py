from collections import Counter

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        top_cnt, bottom_cnt = Counter(tops), Counter(bottoms)
        ans = 99999
        for x in (tops[0], bottoms[0]):
            if all(t == x or b == x for t, b in zip(tops, bottoms)) and top_cnt[x] + bottom_cnt[x] >= n:
                ans = n - max(top_cnt[x], bottom_cnt[x])
        return -1 if ans == 99999 else ans
