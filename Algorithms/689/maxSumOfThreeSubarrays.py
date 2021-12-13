class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ans = []
        sum1, max_sum1, max_sum1_idx = 0, 0, 0
        sum2, max_sum12, max_sum12_idx = 0, 0, []
        sum3, max_total = 0, 0
        for i in range(2 * k, len(nums)):
            sum1 += nums[i - 2 * k]
            sum2 += nums[i - k]
            sum3 += nums[i]
            if i >= 3 * k - 1:
                if sum1 > max_sum1:
                    max_sum1 = sum1
                    max_sum1_idx = i - 3 * k + 1
                if max_sum1 + sum2 > max_sum12:
                    max_sum12 = max_sum1 + sum2
                    max_sum12_idx = [max_sum1_idx, i - 2 * k + 1]
                if max_sum12 + sum3 > max_total:
                    max_total = max_sum12 + sum3
                    ans = [*max_sum12_idx, i - k + 1]
                sum1 -= nums[i - 3 * k + 1]
                sum2 -= nums[i - 2 * k + 1]
                sum3 -= nums[i - k + 1]
        return ans
