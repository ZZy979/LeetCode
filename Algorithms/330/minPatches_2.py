# 评论区解法：补充一个数x，可覆盖范围从[1, k]变成[1, k+x]
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        k = 0  # 当前可覆盖范围[1, k]
        ans = 0
        i, p = 1, 0
        while i <= n:
            if p >= len(nums) or i < nums[p]:
                ans += 1
                k += i
            else:
                k += nums[p]
                p += 1
            i = k + 1
        return ans
