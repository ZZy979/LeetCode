import math

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)
        return max(
            max((nums[i][i] for i in range(n) if is_prime(nums[i][i])), default=0),
            max((nums[i][n - i - 1] for i in range(n) if is_prime(nums[i][n - i - 1])), default=0)
        )

def is_prime(x):
    return x > 1 and not any(x % i == 0 for i in range(2, math.isqrt(x) + 1))
