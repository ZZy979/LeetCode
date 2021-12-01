# n!结尾0的个数 = 1~n中因子5的个数 = [n/5]+[n/5^2]+[n/5^3]+...
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        while n:
            n //= 5
            zeros += n
        return zeros
