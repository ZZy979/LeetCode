# 56 ms
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        n = len(s)
        ans = []
        last = None
        start = -1
        for i in range(n):
            if s[i] != last:
                if start != -1 and i - start >= 3:
                    ans.append([start, i - 1])
                last = s[i]
                start = i
        if n - start >= 3:
            ans.append([start, n - 1])
        return ans
