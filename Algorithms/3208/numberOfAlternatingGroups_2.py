# 官方题解：模拟，时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        res, cnt = 0, 1
        for i in range(-k + 2, n):
            if colors[i] != colors[i - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                res += 1
        return res
