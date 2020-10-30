# 方法2：递归
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return get_subsets(nums, len(nums) - 1)


def get_subsets(nums, index):
    if index == -1:
        return [[]]
    else:
        subsets = get_subsets(nums, index - 1)
        return subsets + [subset + [nums[index]] for subset in subsets]
