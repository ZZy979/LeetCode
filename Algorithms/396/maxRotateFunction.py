class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n, s = len(nums), sum(nums)
        ans = f = sum(map(operator.mul, range(n), nums))
        for i in range(1, n):
            f += s - n * nums[-i]
            ans = max(ans, f)
        return ans
