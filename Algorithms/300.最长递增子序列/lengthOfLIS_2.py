import bisect

# 官方题解：贪心+二分查找
# 时间复杂度O(nlog n)，空间复杂度O(n)
# 48 ms
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []  # d[i]示长度为i的最长上升子序列的末尾元素的最小值
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                d[bisect.bisect_left(d, n)] = n
        return len(d)
