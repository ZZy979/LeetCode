from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(map(str, nums), key=cmp_to_key(cmp))
        return '0' if nums[0] == '0' else ''.join(nums)


def cmp(s, t):
    return int(t + s) - int(s + t)
