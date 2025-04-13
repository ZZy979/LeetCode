class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        return sum(is_symmetric(x) for x in range(low, high + 1))

def is_symmetric(x):
    s = list(map(int, str(x)))
    n = len(s)
    return n % 2 == 0 and sum(s[:n // 2]) == sum(s[n // 2:])
