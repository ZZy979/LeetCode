# 回溯，时间复杂度O(n!)
# 296 ms
class Solution:
    def countArrangement(self, n: int) -> int:
        self.candidate = [[j for j in range(1, n + 1) if i > 0 and (i % j == 0 or j % i == 0)] for i in range(n + 1)]
        self.ans = 0
        self.backtrack(1, n, [False] * (n + 1))
        return self.ans
    
    def backtrack(self, i, n, used):
        if i > n:
            self.ans += 1
            return
        for j in self.candidate[i]:
            if not used[j]:
                used[j] = True
                self.backtrack(i + 1, n, used)
                used[j] = False
