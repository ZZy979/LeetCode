import bisect

# 官方题解：最长递增子序列
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        n = len(target)
        pos = {x: i for i, x in enumerate(target)}
        d = []
        for x in arr:
            if x in pos:
                idx = pos[x]
                if not d or idx > d[-1]:
                    d.append(idx)
                else:
                    d[bisect.bisect_left(d, idx)] = idx
        return n - len(d)
