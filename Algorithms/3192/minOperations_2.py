class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            if ans % 2 == x:
                ans += 1
        return ans
