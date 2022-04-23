class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        idx = [i for i in range(len(s)) if s[i] == c]
        ans = [0] * len(s)
        ans[:idx[0]] = range(idx[0], 0, -1)
        for i in range(len(idx) - 1):
            if (d := idx[i + 1] - idx[i] - 1) % 2 == 0:
                ans[idx[i] + 1:idx[i] + d // 2 + 1] = range(1, d // 2 + 1)
                ans[idx[i] + d // 2 + 1:idx[i + 1]] = range(d // 2, 0, -1)
            else:
                ans[idx[i] + 1:idx[i] + d // 2 + 1] = range(1, d // 2 + 1)
                ans[idx[i] + d // 2 + 1] = (d + 1) // 2
                ans[idx[i] + d // 2 + 2:idx[i + 1]] = range(d // 2, 0, -1)
        ans[idx[-1] + 1:] = range(1, len(s) - idx[-1])
        return ans
