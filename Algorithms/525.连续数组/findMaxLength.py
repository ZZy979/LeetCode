class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        m = {0: -1}
        pre = ans = 0
        for i, x in enumerate(nums):
            pre += 1 if x == 1 else -1
            if pre in m:
                ans = max(ans, i - m[pre])
            else:
                m[pre] = i
        return ans
