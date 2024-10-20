# 官方题解：动态规划+二分查找
class Solution:
    def __init__(self):
        self.memo = {}

    def superEggDrop(self, k: int, n: int) -> int:
        return self.dp(k, n)
    
    def dp(self, k, n):
        if (k, n) in self.memo:
            return self.memo[k, n]
        if n == 0:
            ans = 0
        elif k == 1:
            ans = n
        else:
            lo, hi = 1, n
            while hi - lo > 1:
                x = (lo + hi) // 2
                t1 = self.dp(k - 1, x - 1)
                t2 = self.dp(k, n - x)
                if t1 < t2:
                    lo = x
                elif t1 > t2:
                    hi = x
                else:
                    lo = hi = x
            ans = 1 + min(max(self.dp(k - 1, x - 1), self.dp(k, n - x)) for x in (lo, hi))
            self.memo[k, n] = ans
        return ans
