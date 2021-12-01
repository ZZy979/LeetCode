class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry == 0:
                break
            else:
                carry, digits[i] = divmod(digits[i] + carry, 10)
        if carry:
            digits.insert(0, carry)
        return digits
