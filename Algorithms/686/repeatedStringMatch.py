class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeat, max_repeat = 1, len(b) // len(a) + 2
        s = a
        while repeat <= max_repeat:
            if b in s:
                return repeat
            else:
                repeat += 1
                s += a
        return -1
