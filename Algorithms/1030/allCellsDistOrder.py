# 直接排序，时间复杂度O(RClog(RC))
# 156 ms
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dist = [(abs(r - r0) + abs(c - c0), r, c) for r in range(R) for c in range(C)]
        dist.sort()
        return [(r, c) for d, r, c in dist]
