class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not 0 < k <= n:
            return []
        elif k == 1:
            return [[i] for i in range(1, n + 1)]
        elif k == n:
            return [list(range(1, n + 1))]
        else:
            return self.combine(n - 1, k) + [c + [n] for c in self.combine(n - 1, k - 1)]
