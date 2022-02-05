class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = max(min(l, w) for l, w in rectangles)
        return sum(min(l, w) == max_len for l, w in rectangles)
