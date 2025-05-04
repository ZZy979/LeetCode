# 滑动窗口+乘法原理，时间复杂度O(n)，空间复杂度O(n)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        pos = [i for i in range(len(nums)) if nums[i] == mx]
        pos.append(len(nums)) # 把nums数组长度加入pos末尾，方便计算最后一段的长度
        return sum((pos[i] + 1) * (pos[i + k] - pos[i + k - 1]) for i in range(len(pos) - k))
