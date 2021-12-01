# 方法2：二分查找，时间复杂度O(n)
# 32 ms
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        p = binsearch(nums, target)
        if p == -1:
            return [-1, -1]
        n = len(nums)
        begin = end = p
        while begin >= 1 and nums[begin - 1] == target:
            begin -= 1
        while end <= n - 2 and nums[end + 1] == target:
            end += 1
        return [begin, end]


def binsearch(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
