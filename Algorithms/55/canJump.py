# 计算可达性，时间复杂度O(sum(nums))
# 4600 ms
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reachable = [False] * n
        reachable[0] = True
        for i in range(n - 1):
            if reachable[i]:
                for j in range(1, nums[i] + 1):
                    if i + j == n - 1:
                        return True
                    reachable[i + j] = True
        return reachable[-1]
