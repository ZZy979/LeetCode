from collections import Counter

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = Counter(deliciousness)
        m = max(count)
        pows = [p for i in range(22) if (p := pow(2, i)) <= 2 * m]
        q = 10**9 + 7
        return (sum(count[i] * count[p - i] for i in count for p in pows if p > 2 * i) \
            + sum(count[i] * (count[i] - 1) // 2 for i in count if 2 * i in pows)) % q
