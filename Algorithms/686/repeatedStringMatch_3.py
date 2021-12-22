class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if set(b) - set(a):
            return -1
        s = 2 * (len(b) // len(a) + 1) * a
        idx = s.find(b)
        if idx == -1:
            return -1
        d, m = divmod(idx + len(b), len(a))
        return d if m == 0 else d + 1
