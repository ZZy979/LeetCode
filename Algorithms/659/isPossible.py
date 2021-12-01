from collections import defaultdict

# 官方题解1：哈希表+最小堆
# 时间复杂度O(nlog n)，空间复杂度O(n)
# 216 ms
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        mp = defaultdict(list)
        for x in nums:
            if queue := mp.get(x - 1):
                prev_length = heapq.heappop(queue)
                heapq.heappush(mp[x], prev_length + 1)
            else:
                heapq.heappush(mp[x], 1)
        
        return not any(queue and queue[0] < 3 for queue in mp.values())
