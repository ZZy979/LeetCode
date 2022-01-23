from functools import lru_cache
from itertools import accumulate

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        presum = list(accumulate(piles, initial=0))

        @lru_cache(None)
        def dfs(start, m):
            if start == len(piles):
                return 0, 0
            alice, bob = 0, 0x7fffffff
            for i in range(start + 1, min(start + 2 * m, len(piles)) + 1):
                alice_got = presum[i] - presum[start]
                bob_new, alice_new = dfs(i, max(m, i - start))
                if alice_got + alice_new - bob_new > alice - bob:
                    alice, bob = alice_got + alice_new, bob_new
            return alice, bob
        
        return dfs(0, 1)[0]
