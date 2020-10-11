class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        for m in (2, 3, 5):
            while num % m == 0:
                num //= m
        return num == 1
