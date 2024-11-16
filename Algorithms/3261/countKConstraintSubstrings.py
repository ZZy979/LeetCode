# 官方题解：滑动窗口+前缀数组
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        count = [0, 0]
        prefix = [0] * (n + 1)
        right = [n] * n
        i = 0
        for j in range(n):
            count[int(s[j])] += 1
            while count[0] > k and count[1] > k:
                count[int(s[i])] -= 1
                right[i] = j
                i += 1
            prefix[j + 1] = prefix[j] + j - i + 1
        
        res = []
        for l, r in queries:
            i = min(right[l], r + 1)
            part1 = (i - l + 1) * (i - l) // 2
            part2 = prefix[r + 1] - prefix[i]
            res.append(part1 + part2)
        return res
