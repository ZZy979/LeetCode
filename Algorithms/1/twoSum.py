class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {x: i for i, x in enumerate(nums)}
        for i, x in enumerate(nums):
            y = target - x
            if y in index and index[y] != i:
                return [i, index[y]]
