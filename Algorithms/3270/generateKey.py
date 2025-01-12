class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        return min(num1 // 1000, num2 // 1000, num3 // 1000) * 1000 \
            + min(num1 // 100 % 10, num2 // 100 % 10, num3 // 100 % 10) * 100 \
            + min(num1 // 10 % 10, num2 // 10 % 10, num3 // 10 % 10) * 10 \
            + min(num1 % 10, num2 % 10, num3 % 10)
