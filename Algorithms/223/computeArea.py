class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        s = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        if bx2 <= ax1 or bx1 >= ax2 or by2 <= ay1 or by1 >= ay2:
            return s
        else:
            # ax1 <= bx1 < ax2
            return s - (min(ax2, bx2) - max(ax1, bx1)) * (min(ay2, by2) - max(ay1, by1))
