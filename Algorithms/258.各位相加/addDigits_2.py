class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else 9 if num % 9 == 0 else num % 9
