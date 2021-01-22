# 官方题解2：前缀和
# 时间复杂度O(n)，空间复杂度O(n)
# 288 ms
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        p = list(itertools.accumulate(A, initial=0))
        count = collections.Counter()
        ans = 0
        for x in p:
            ans += count[x]
            count[x + S] += 1
        return ans
