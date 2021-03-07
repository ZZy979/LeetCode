class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        for i in range(len(digits) - 2, -1, -1):
            if digits[i] < digits[i + 1]:
                for j in range(len(digits) - 1, i, -1):
                    if digits[j] > digits[i]:
                        digits[i], digits[j] = digits[j], digits[i]
                        digits[i + 1:] = list(reversed(digits[i + 1:]))
                        m = int(''.join(digits))
                        return m if m <= 0x7fffffff else -1
        return -1
