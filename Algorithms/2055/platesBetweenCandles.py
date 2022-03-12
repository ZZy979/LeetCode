# 官方题解：预处理+前缀和
# 时间复杂度O(n+q)，空间复杂度O(n)
# 232 ms
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        pre_sum, p = [0] * n, 0
        left, l = [0] * n, -1
        for i, c in enumerate(s):
            if c == '*':
                p += 1
            else:
                l = i
            pre_sum[i] = p
            left[i] = l
        
        right, r = [0] * n, -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                r = i
            right[i] = r
        
        ans = [0] * len(queries)
        for i, (l, r) in enumerate(queries):
            x, y = right[l], left[r]
            if x >= 0 and y >= 0 and x < y:
                ans[i] = pre_sum[y] - pre_sum[x]
        return ans
