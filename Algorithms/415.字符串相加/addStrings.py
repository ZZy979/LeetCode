class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        a = [ord(c) - ord('0') for c in reversed(num1)]
        b = [ord(c) - ord('0') for c in reversed(num2)]
        carry = 0
        s = [0] * len(a)
        for i in range(len(b)):
            carry, s[i] = divmod(a[i] + b[i] + carry, 10)
        for i in range(len(b), len(a)):
            carry, s[i] = divmod(a[i] + carry, 10)
        if carry:
            s.append(carry)
        return ''.join(chr(ord('0') + x) for x in reversed(s))
