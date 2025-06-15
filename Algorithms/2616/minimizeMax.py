# 官方题解：二分答案+贪心
# 时间复杂度O(nlog n+nlog U)，空间复杂度O(1)，其中U=max(nums)-min(nums)
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if check(nums, p, mid):
                right = mid
            else:
                left = mid + 1
        return left

def check(nums, p, mx):
    cnt = 0
    i = 0
    while i < len(nums) - 1:
        if nums[i + 1] - nums[i] <= mx:
            cnt += 1
            i += 2
        else:
            i += 1
    return cnt >= p
