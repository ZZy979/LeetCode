class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        a = ['' for i in range(numRows)]
        r = 0
        direction = 1  # 1-下,-1-右上
        for c in s:
            a[r] += c
            r += direction
            if r == 0 or r == numRows - 1:
                direction = -direction
        return ''.join(a)
