# 归并排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        merge_sort(nums, 0, len(nums) - 1)
        return nums


def merge_sort(nums, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)
    temp = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if nums[i] < nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
    while i <= mid:
        temp.append(nums[i])
        i += 1
    while j <= right:
        temp.append(nums[j])
        j += 1
    nums[left:right + 1] = temp
