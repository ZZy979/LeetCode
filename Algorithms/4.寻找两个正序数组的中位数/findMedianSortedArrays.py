class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = merge(nums1, nums2)
        n = len(nums)
        return nums[n // 2] if n % 2 == 1 else (nums[n // 2] + nums[n // 2 - 1]) / 2


def merge(a, b):
    res = [0] * (len(a) + len(b))
    i = j = k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res[k] = a[i]
            i += 1
        else:
            res[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        res[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        res[k] = b[j]
        j += 1
        k += 1
    return res
