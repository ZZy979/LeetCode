# 快速排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        quick_sort(nums, 0, len(nums) - 1)
        return nums


def partition(nums, left, right):
    pivot = nums[right]
    p = left
    for i in range(left, right):
        if nums[i] < pivot:
            nums[p], nums[i] = nums[i], nums[p]
            p += 1
    nums[p], nums[right] = nums[right], nums[p]
    return p

def quick_sort(nums, left, right):
    if left >= right:
        return
    p = partition(nums, left, right)
    quick_sort(nums, left, p - 1)
    quick_sort(nums, p + 1, right)
