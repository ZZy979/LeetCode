class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = sum(set(nums))
        return [sum(nums) - s, n * (n + 1) // 2 - s]
