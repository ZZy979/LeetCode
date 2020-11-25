# 方法1：直接排序，前后交替取元素
# 时间复杂度O(nlog n)，空间复杂度O(n)
# 44 ms
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = list(sorted(nums))
        n = len(tmp)
        i = 0
        for j in range(n // 2):
            nums[i] = tmp[j]
            nums[i + 1] = tmp[-(j + 1)]
            i += 2
        if n % 2 == 1:
            nums[i] = tmp[n // 2]
