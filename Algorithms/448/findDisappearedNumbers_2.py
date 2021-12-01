# 官方题解：原地修改
# 时间复杂度O(n)，空间复杂度O(1)
# 376 ms
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for x in nums:
            nums[(x - 1) % n] += n
        return [i + 1 for i, x in enumerate(nums) if x <= n]
