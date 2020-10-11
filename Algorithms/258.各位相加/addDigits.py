class Solution:
    def addDigits(self, num: int) -> int:
        s = 0
        while num > 0:
            s += num % 10
            num //= 10
        return s if s < 10 else self.addDigits(s)
