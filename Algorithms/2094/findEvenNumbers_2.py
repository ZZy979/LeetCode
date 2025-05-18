from collections import Counter

# 官方题解：遍历所有可能的3位偶数
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        freq = Counter(digits)
        for i in range(100, 1000, 2):
            c = Counter(int(d) for d in str(i))
            if all(freq[d] >= c[d] for d in c):
                res.append(i)
        return res
