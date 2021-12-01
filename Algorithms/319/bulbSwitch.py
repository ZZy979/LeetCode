class Solution:
    def bulbSwitch(self, n: int) -> int:
        return 0 if n == 0 else math.isqrt(n)
