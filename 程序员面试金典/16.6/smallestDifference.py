import bisect

# 方法1：二分查找，时间复杂度O((a+b)log b)
# 228 ms
class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        b.sort()
        min_diff = 0x7fffffff
        for x in a:
            i = bisect.bisect(b, x)
            if i < len(b) and b[i] == x:
                return 0
            else:
                if i > 0:
                    min_diff = min(min_diff, x - b[i - 1])
                if i < len(b):
                    min_diff = min(min_diff, b[i] - x)
        return min_diff
