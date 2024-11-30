# 双指针，时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        left = right = ans = 0
        while left < n:
            right += 1
            if colors[right % n] == 1 - colors[(right - 1) % n]:
                if right - left >= k - 1:
                    ans += 1
                    left += 1
            else:
                left = right
        return ans
