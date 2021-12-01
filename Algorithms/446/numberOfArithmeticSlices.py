# 官方题解：动态规划+哈希表
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        f = [defaultdict(int) for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                d = nums[i] - nums[j]
                ans += f[j][d]
                f[i][d] += f[j][d] + 1
        return ans
