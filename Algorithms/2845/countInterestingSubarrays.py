from collections import Counter

# 前缀和，时间复杂度O(n)，空间复杂度O(min(n, modulo))
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        prefix_cnt = 0  # count[i]表示nums[0:i]中满足nums[i] % modulo == k的个数
        cnt = Counter([0])  # count[i]的出现次数
        ans = 0
        for i in range(n):
            prefix_cnt += nums[i] % modulo == k
            # (count[i] - count[j]) % modulo == k 等价于 count[j] % modulo = (count[i] + modulo - k) % modulo
            ans += cnt[(prefix_cnt + modulo - k) % modulo]
            cnt[prefix_cnt % modulo] += 1
        return ans
