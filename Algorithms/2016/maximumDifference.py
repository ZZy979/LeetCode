class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_num, max_diff = 0x7fffffff, 0
        for x in nums:
            min_num = min(min_num, x)
            max_diff = max(max_diff, x - min_num)
        return -1 if max_diff == 0 else max_diff
