class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        negative = num < 0
        num = abs(num)
        digits = []
        while num > 0:
            digits.append(str(num % 7))
            num //= 7
        if negative:
            digits.append('-')
        return ''.join(reversed(digits))
