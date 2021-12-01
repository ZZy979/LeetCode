from collections import Counter

# 官方题解2：哈希表+滑动窗口+位运算
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        b = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        if len(s) <= 10:
            return []
        ans = []
        x = 0
        for c in s[:9]:
            x = (x << 2) | b[c]
        count = Counter()
        for i in range(len(s) - 9):
            x = ((x << 2) | b[s[i + 9]]) & ((1 << 20) - 1)
            count[x] += 1
            if count[x] == 2:
                ans.append(s[i:i + 10])
        return ans
