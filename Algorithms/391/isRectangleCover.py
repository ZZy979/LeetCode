from collections import Counter

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area, min_x, min_y, max_x, max_y = 0, 99999, 99999, -99999, -99999
        count = Counter()
        for x, y, a, b in rectangles:
            area += (a - x) * (b - y)

            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, a)
            max_y = max(max_y, b)

            count[(x, y)] += 1
            count[(x, b)] += 1
            count[(a, y)] += 1
            count[(a, b)] += 1
        if area != (max_x - min_x) * (max_y - min_y) or count[(min_x, min_y)] != 1 or count[(min_x, max_y)] != 1 or count[(max_x, min_y)] != 1 or count[(max_x, max_y)] != 1:
            return False
        del count[(min_x, min_y)], count[(min_x, max_y)], count[(max_x, min_y)], count[(max_x, max_y)]
        return all(c == 2 or c == 4 for c in count.values())
