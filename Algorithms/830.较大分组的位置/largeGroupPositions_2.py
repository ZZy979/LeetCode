# 官方题解，48 ms
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ret = []
        n, num = len(s), 1
        for i in range(n):
            if i == n - 1 or s[i] != s[i + 1]:
                if num >= 3:
                    ret.append([i - num + 1, i])
                num = 1
            else:
                num += 1
        return ret
