# 官方题解：双指针
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ans = []
        l, r = 1, 2
        while l < r:
            s = (l + r) * (r - l + 1) // 2
            if s == target:
                ans.append(list(range(l, r + 1)))
                l += 1
            elif s < target:
                r += 1
            else:
                l += 1
        return ans
