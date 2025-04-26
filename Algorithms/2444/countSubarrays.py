from sortedcontainers import SortedList

# 滑动窗口，时间复杂度O(nlog n)，空间复杂度O(n)
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        if minK > maxK:
            return 0
        n = len(nums)
        begin = end = ans = 0
        while begin < n and end < n:
            begin = end
            while begin < n and (nums[begin] < minK or nums[begin] > maxK):
                begin += 1
            end = begin
            while end < n and minK <= nums[end] <= maxK:
                end += 1
            ans += count(nums, begin, end, minK, maxK)
        return ans

def count(nums, begin, end, minK, maxK):
    """计算nums[begin:end]中的定界子数组的数目，其中每个元组都在[minK, maxK]范围内"""
    window = SortedList()
    res = 0
    right = begin
    for left in range(begin, end):
        while right < end and (not window or window[0] != minK or window[-1] != maxK):
            window.add(nums[right])
            right += 1
        if window[0] == minK and window[-1] == maxK:
            res += end - right + 1
        window.remove(nums[left])
    return res
