from collections import Counter

# 官方题解2：基于计数的贪心算法
# 时间复杂度O(n)，空间复杂度O(n)
# 40 ms
class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) < 2:
            return S
        length = len(S)
        counts = Counter(S)
        maxCount = max(counts.items(), key=lambda x: x[1])[1]
        if maxCount > (length + 1) // 2:
            return ''

        reorganizeArray = [''] * length
        evenIndex, oddIndex = 0, 1
        halfLength = length // 2
        for c, count in counts.items():
            while count > 0 and count <= halfLength and oddIndex < length:
                reorganizeArray[oddIndex] = c
                count -= 1
                oddIndex += 2
            while count > 0:
                reorganizeArray[evenIndex] = c
                count -= 1
                evenIndex += 2
        return ''.join(reorganizeArray)
