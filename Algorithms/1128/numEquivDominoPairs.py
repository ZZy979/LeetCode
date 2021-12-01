from collections import Counter

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        c = Counter()
        ans = 0
        for a, b in dominoes:
            val = (10 * a + b if a <= b else 10 * b + a)
            ans += c[val]
            c[val] += 1
        return ans
