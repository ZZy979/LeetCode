class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res, imax, dmax = 0, 0, 0  # imax为nums[i]的最大值，dmax为nums[i]-nums[j]的最大值
        for k in range(len(nums)):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return res
