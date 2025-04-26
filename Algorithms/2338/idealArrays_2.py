import math

# https://leetcode.cn/problems/count-the-number-of-ideal-arrays/solutions/1659088/shu-lun-zu-he-shu-xue-zuo-fa-by-endlessc-iouh/
# 组合数学，时间复杂度O(Mlog log M)，空间复杂度O(1)
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        q = 10**9 + 7
        ans = 0
        for x in range(1, maxValue + 1):
            res = 1
            for e in prime_factor_pow(x):
                res = res * math.comb(n + e - 1, e) % q
            ans = (ans + res) % q
        return ans

def prime_factor_pow(n):
    """返回n质因数分解后每个质因数的幂"""
    pows = []
    i = 2
    while i * i <= n:
        e = 0
        while n % i == 0:
            e += 1
            n //= i
        if e > 0:
            pows.append(e)
        i += 1
    if n > 1:
        pows.append(1)
    return pows
