class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = (len(a) + len(b) - 1) // len(a)
        if b in n * a:
            return n
        elif b in (n + 1) * a:
            return n + 1
        else:
            return -1
