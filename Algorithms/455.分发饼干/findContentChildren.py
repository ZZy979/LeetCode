# 排序+贪心，时间复杂度O(|g|log |g| + |s|log |s|)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        for j in range(len(s)):
            if i >= len(g):
                break
            if s[j] >= g[i]:
                i += 1
        return i
