class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        return int(''.join(min(d) for d in zip(*[f'{x:04d}' for x in (num1, num2, num3)])))
