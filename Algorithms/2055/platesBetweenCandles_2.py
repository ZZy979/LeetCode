import bisect

# 二分查找
# 时间复杂度O(n+qlog n)，空间复杂度O(n)
# 304 ms
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = [i for i, c in enumerate(s) if c == '|']
        ans = []
        for l, r in queries:
            x = bisect.bisect_left(candles, l)
            y = bisect.bisect_right(candles, r) - 1
            if y <= x:
                ans.append(0)
            else:
                num_candles = y - x + 1
                num_slots = candles[y] - candles[x] + 1
                ans.append(num_slots - num_candles)
        return ans
