class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        return sum(is_symmetric(x) for x in range(low, high + 1))

def is_symmetric(x):
    return x < 100 and x % 11 == 0 or 1000 <= x < 10000 and x // 1000 + x % 1000 // 100 == x % 100 // 10 + x % 10
