# 散列表（集合）
# 时间复杂度O(n)，空间复杂度O(n)
# 364 ms
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))
