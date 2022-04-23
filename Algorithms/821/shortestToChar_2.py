# 官方题解：两次遍历
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0] * n
        
        idx = -n
        for i in range(n):
            if s[i] == c:
                idx = i
            ans[i] = i - idx
        
        idx = 2 * n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                idx = i
            ans[i] = min(ans[i], idx - i)
        return ans
