class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = [0] * n
        return mergeSort(nums, tmp, 0, n - 1)


def mergeSort(nums, tmp, left, right):
    if left >= right:
        return 0
    mid = (left + right) // 2
    rev_count = mergeSort(nums, tmp, left, mid) + mergeSort(nums, tmp, mid + 1, right)
    i, j, p = left, mid + 1, left
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            tmp[p] = nums[i]
            i += 1
            rev_count += j - (mid + 1)
        else:
            tmp[p] = nums[j]
            j += 1
        p += 1
    while i <= mid:
        tmp[p] = nums[i]
        rev_count += j - (mid + 1)
        i += 1
        p += 1
    while j <= right:
        tmp[p] = nums[j]
        j += 1
        p += 1
    nums[left:right + 1] = tmp[left:right + 1]
    return rev_count
