class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        return 1 if a == e and not (c == e and min(b, f) < d < max(b, f)) \
            or b == f and not (d == f and min(a, e) < c < max(a, e)) \
            or c - d == e - f and not (a - b == e - f and min(c, e) < a < max(c, e)) \
            or c + d == e + f and not (a + b == e + f and min(c, e) < a < max(c, e)) \
            else 2
