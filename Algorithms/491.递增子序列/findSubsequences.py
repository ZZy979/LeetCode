class Solution:
    def __init__(self):
        self.ans = []
        self.temp = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.dfs(0, -101, nums)
        return self.ans
    
    def dfs(self, cur, last, nums):
        if cur == len(nums):
            if len(self.temp) >= 2:
                self.ans.append(self.temp.copy())
            return
        if nums[cur] >= last:
            self.temp.append(nums[cur])
            self.dfs(cur + 1, nums[cur], nums)
            self.temp.pop()
        if nums[cur] != last:
            self.dfs(cur + 1, last, nums)
