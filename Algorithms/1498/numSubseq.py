import bisect

# 官方题解：枚举最小值+二分查找，时间复杂度O(nlog n)，空间复杂度O(n)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        q = 10**9 + 7
        f = [1] + [0] * (n - 1)  # f[i] = 2^i % q
        for i in range(1, n):
            f[i] = f[i - 1] * 2 % q

        nums.sort()
        ans = 0
        for i, num in enumerate(nums):
            if num * 2 > target:
                break
            max_value = target - num
            pos = bisect.bisect_right(nums, max_value) - 1
            ans = (ans + f[max(0, pos - i)]) % q
        return ans % q
