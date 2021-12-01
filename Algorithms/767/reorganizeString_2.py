import heapq
from collections import Counter

# 官方题解1：基于最大堆的贪心算法（每次取两个出现次数最多的字母）
# 时间复杂度O(nlog n)，空间复杂度O(n)
# 36 ms
class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) < 2:
            return S
        counts = Counter(S)
        if counts.most_common(1)[0][1] > (len(S) + 1) // 2:
            return ''

        queue = [(-n, k) for k, n in counts.items()]
        heapq.heapify(queue)
        ans = []
        while len(queue) > 1:
            n1, k1 = heapq.heappop(queue)
            n2, k2 = heapq.heappop(queue)
            ans.extend([k1, k2])
            n1 += 1
            n2 += 1
            if n1 < 0:
                heapq.heappush(queue, (n1, k1))
            if n2 < 0:
                heapq.heappush(queue, (n2, k2))
        if queue:
            ans.append(queue[0][1])
        return ''.join(ans)
