# 贪心，时间复杂度O((m+n)log(m+n))
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        cuts = [0, 0]
        cost = sorted([(c, 0) for c in horizontalCut] + [(c, 1) for c in verticalCut], reverse=True)
        ans = 0
        for c, t in cost:
            ans += c * (cuts[1 - t] + 1)
            cuts[t] += 1
        return ans
