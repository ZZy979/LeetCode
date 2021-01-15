class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        n = 0
        ans = []
        for x in A:
            n = ((n << 1) + x) % 5
            ans.append(n == 0)
        return ans
