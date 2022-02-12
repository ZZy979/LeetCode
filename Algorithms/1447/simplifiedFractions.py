import math

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return [f'{b}/{a}' for a in range(2, n + 1) for b in range(1, a) if math.gcd(a, b) == 1]
