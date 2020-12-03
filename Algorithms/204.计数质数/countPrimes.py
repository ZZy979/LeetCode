import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                is_prime[i * i:n:i] = [False] * len(range(i * i, n, i))
        return sum(is_prime)
