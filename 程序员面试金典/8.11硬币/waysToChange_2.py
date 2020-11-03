# 方法2：记忆DFS，限制最大币值
# 1204 ms
class Solution:
    def __init__(self):
        self.memo = {}
    
    def waysToChange(self, n: int) -> int:
        return self.ways(n, 25)
        
    def ways(self, n, m):
        if m == 1 or n <= 4:
            return 1
        elif (n, m) in self.memo:
            return self.memo[(n, m)]
        ans = 0
        for a in (25, 10, 5, 1):
            if a <= m and n >= a:
                ans += self.ways(n - a, a)
                ans %= 1000000007
        self.memo[(n, m)] = ans
        return ans
