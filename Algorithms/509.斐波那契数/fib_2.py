class Solution:
    def fib(self, n: int) -> int:
        sqrt5 = 5 ** 0.5
        return round((((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n) / sqrt5)
