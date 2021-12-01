class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n //= 10
            if s == 1:
                return True
            elif s in seen:
                return False
            else:
                seen.add(s)
                n = s
