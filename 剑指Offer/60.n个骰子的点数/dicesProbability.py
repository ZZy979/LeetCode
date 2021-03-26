from collections import defaultdict

class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        freq = {0: 1}
        for _ in range(n):
            new_freq = defaultdict(int)
            for i in range(1, 7):
                for s in freq:
                    new_freq[i + s] += freq[s]
            freq = new_freq
        total = 6**n
        return [freq[s] / total for s in range(n, 6 * n + 1)]
