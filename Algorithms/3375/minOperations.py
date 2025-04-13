class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return -1 if k > min(nums) else len(set(x for x in nums if x > k))
