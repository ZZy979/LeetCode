class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        x11, y11 = start1
        x12, y12 = end1
        x21, y21 = start2
        x22, y22 = end2
        if x11 == x12 and x21 == x22:
            # line1: x = x11, line2: x = x21
            if x11 != x21:
                return []
            else:
                y = interval_intersection(min(y11, y12), max(y11, y12), min(y21, y22), max(y21, y22))
                return [] if y is None else [x11, y]
        elif x11 == x12:
            # line1: x = x11, line2: y - y21 = (y22 - y21)(x - x21) / (x22 - x21)
            y = (y22 - y21) * (x11 - x21) / (x22 - x21) + y21
            return [x11, y] if min(x21, x22) <= x11 <= max(x21, x22) and min(y11, y12) <= y <= max(y11, y12) else []
        elif x21 == x22:
            # line1: y - y11 = (y12 - y11)(x - x11) / (x12 - x11), line2: x = x21
            y = (y12 - y11) * (x21 - x11) / (x12 - x11) + y11
            return [x21, y] if min(x11, x12) <= x21 <= max(x11, x12) and min(y21, y22) <= y <= max(y21, y22) else []
        else:
            # line1: y = k1 * x + b1, line2: y = k2 * x + b2
            k1 = (y12 - y11) / (x12 - x11)
            b1 = y11 - k1 * x11
            k2 = (y22 - y21) / (x22 - x21)
            b2 = y21 - k2 * x21
            if k1 == k2:
                if b1 != b2:
                    return []
                else:
                    x = interval_intersection(min(x11, x12), max(x11, x12), min(x21, x22), max(x21, x22))
                    return [x, k1 * x + b1] if x is not None else []
            else:
                x = (b2 - b1) / (k1 - k2)
                return [x, k1 * x + b1] if min(x11, x12) <= x <= max(x11, x12) and min(x21, x22) <= x <= max(x21, x22) else []


def interval_intersection(a1, b1, a2, b2):
    return None if a1 > b2 or a2 > b1 else max(a1, a2)
