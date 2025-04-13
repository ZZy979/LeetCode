from collections import Counter
from math import factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        dictionary = set()
        base = 10 ** ((n - 1) // 2)
        skip = n & 1
        # 枚举n个数位的回文数左半边
        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]
            if int(s) % k == 0:
                # 是k回文数
                dictionary.add(''.join(sorted(s)))

        fac = [factorial(i) for i in range(n + 1)]
        ans = 0
        for s in dictionary:
            cnt = Counter(s)
            tot = (n - cnt['0']) * fac[n - 1]
            for x in cnt.values():
                tot //= fac[x]
            ans += tot
        return ans
