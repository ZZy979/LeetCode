class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        miss_sum = mean * (n + len(rolls)) - sum(rolls)
        if n <= miss_sum <= 6 * n:
            k, r = divmod(miss_sum, n)
            return [k + 1] * r + [k] * (n - r)
        else:
            return []
