# 官方题解：二分查找
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        return (get_kth_element(nums1, nums2, (n + 1) // 2) + get_kth_element(nums1, nums2, (n + 2) // 2)) / 2


def get_kth_element(nums1, nums2, k):
    i = j = 0
    while True:
        if i == len(nums1):
            return nums2[j + k - 1]
        elif j == len(nums2):
            return nums1[i + k - 1]
        elif k == 1:
            return min(nums1[i], nums2[j])
        
        ni = min(i + k // 2 - 1, len(nums1) - 1)
        nj = min(j + k // 2 - 1, len(nums2) - 1)
        if nums1[ni] <= nums2[nj]:
            k -= ni - i + 1
            i = ni + 1
        else:
            k -= nj - j + 1
            j = nj + 1
