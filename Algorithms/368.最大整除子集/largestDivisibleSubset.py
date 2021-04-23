class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        nums.sort()
        divisible = get_divisible(nums)

        dp = {}
        max_size, start = 0, None
        for x in reversed(nums):
            if not divisible[x]:
                dp[x] = (1, None)
            else:
                max_n, max_y = 0, None
                for y in divisible[x]:
                    if dp[y][0] > max_n:
                        max_n = dp[y][0]
                        max_y = y
                dp[x] = (max_n + 1, max_y)
            if dp[x][0] > max_size:
                max_size = dp[x][0]
                start = x
        
        x = start
        ans = [x]
        while dp[x][1] is not None:
            ans.append(dp[x][1])
            x = dp[x][1]
        return ans


def get_divisible(nums):
    res = {}
    for i in range(len(nums)):
        res[nums[i]] = []
        for j in range(i + 1, len(nums)):
            if nums[j] % nums[i] == 0:
                res[nums[i]].append(nums[j])
    return res
