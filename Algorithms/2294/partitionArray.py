class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        last = nums[0]
        for x in nums:
            if x - last > k:
                ans += 1
                last = x
        return ans + 1
