# 枚举，时间复杂度O(nk)，空间复杂度O(1)
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        ans = set()
        for i in range(n):
            if nums[i] == key:
                ans.update(range(max(0, i - k), min(n, i + k + 1)))
        return sorted(ans)
