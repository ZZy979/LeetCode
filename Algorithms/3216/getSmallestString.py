class Solution:
    def getSmallestString(self, s: str) -> str:
        digits = list(map(int, s))
        for i in range(len(digits) - 1):
            if digits[i] % 2 == digits[i + 1] % 2 and digits[i] > digits[i + 1]:
                digits[i], digits[i + 1] = digits[i + 1], digits[i]
                break
        return ''.join(map(str, digits))
