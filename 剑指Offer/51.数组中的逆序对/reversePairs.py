# 官方题解1：归并排序，时间复杂度O(nlog n)
# 1324 ms
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = [0] * n
        return merge_sort(nums, tmp, 0, n - 1)


def merge_sort(nums, tmp, left, right):
    if left >= right:
        return 0
    m = (left + right) // 2
    res = merge_sort(nums, tmp, left, m) + merge_sort(nums, tmp, m + 1, right)
    i, j = left, m + 1
    tmp[left:right + 1] = nums[left:right + 1]
    for k in range(left, right + 1):
        if i == m + 1:
            nums[k] = tmp[j]
            j += 1
        elif j == right + 1 or tmp[i] <= tmp[j]:
            nums[k] = tmp[i]
            i += 1
            res += j - m - 1
        else:
            nums[k] = tmp[j]
            j += 1
    return res
