class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = n = 0
        for x in nums:
            if x == 1:
                n += 1
            else:
                ans = max(ans, n)
                n = 0
        ans = max(ans, n)
        return ans
