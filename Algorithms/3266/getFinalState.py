import heapq

# 官方题解：优先队列+批量操作优化
# 时间复杂度O(n(log nlog mx + log k/n))，空间复杂度O(n)
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums
        n, m = len(nums), 10**9 + 7
        mx = max(nums)
        v = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(v)
        while v[0][0] < mx and k:
            k -= 1
            num, i = heapq.heappop(v)
            heapq.heappush(v, (num * multiplier, i))
        v.sort()
        for i in range(n):
            t = k // n + (i < k % n)
            nums[v[i][1]] = ((v[i][0] % m) * pow(multiplier, t, m)) % m
        return nums
