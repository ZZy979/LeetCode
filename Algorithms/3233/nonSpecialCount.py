import math

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        return r - l + 1 - num_primes_between(math.ceil(math.sqrt(l)), math.floor(math.sqrt(r)))

def num_primes_between(m, n):
    if n < 2:
        return 0
    is_primes = [False, False] + [True] * (n - 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_primes[i]:
            for j in range(i**2, n + 1, i):
                is_primes[j] = False
    return sum(is_primes[m:n + 1])
