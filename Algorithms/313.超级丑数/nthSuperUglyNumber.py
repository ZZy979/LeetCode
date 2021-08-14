# 动态规划
# 时间复杂度O(nm)，空间复杂度O(n+m)
# 604 ms
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        nums = [1]
        idx = dict.fromkeys(primes, 0)
        for _ in range(n - 1):
            v = min(nums[idx[p]] * p for p in primes)
            nums.append(v)
            for p in primes:
                while nums[idx[p]] * p <= v:
                    idx[p] += 1
        return nums[-1]
