class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums, 0))


def permutations(nums, start):
    if start == len(nums):
        yield []
        return
    for i in range(start, len(nums)):
        nums[start], nums[i] = nums[i], nums[start]
        for p in permutations(nums, start + 1):
            yield [nums[start]] + p
        nums[start], nums[i] = nums[i], nums[start]
