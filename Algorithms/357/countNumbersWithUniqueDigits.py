class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # 各位数字都不相同的n位数有9A(9,n-1)个(2<=n<=10)
        a = [1, 9, 81, 648, 4536, 27216, 136080, 544320, 1632960]
        return sum(a[:n + 1])
