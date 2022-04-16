class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line, width = 1, 0
        for c in s:
            if width + (w := widths[ord(c) - ord('a')]) > 100:
                line += 1
                width = w
            else:
                width += w
        return [line, width]
