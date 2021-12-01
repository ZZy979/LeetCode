# 方法3：将山峰移动到正确位置
# 时间复杂度O(n)，空间复杂度O(1)
# 56 ms
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums), 2):
            max_index = argmax(nums, i - 1, i, i + 1)
            if i != max_index:
                nums[i], nums[max_index] = nums[max_index], nums[i]


def argmax(a, i, j, k):
    ai = a[i] if 0 <= i < len(a) else -0x80000000
    aj = a[j] if 0 <= j < len(a) else -0x80000000
    ak = a[k] if 0 <= k < len(a) else -0x80000000
    m = max(ai, aj, ak)
    return i if ai == m else j if aj == m else k
