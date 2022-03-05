from collections import Counter

# 暴力法，时间复杂度O(n*2^m)，n是字符串个数，m是字符串的平均长度
# 516 ms
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        subseq_count = Counter(''.join(c for j, c in enumerate(s) if (i >> j) & 1) for s in strs for i in range(1 << len(s)))
        return max((len(s) for s, n in subseq_count.items() if n == 1), default=-1)
