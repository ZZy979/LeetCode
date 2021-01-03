# 官方题解1：优先队列
# 时间复杂度O(nlog n)，空间复杂度O(n)
# 600 ms
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        ans = [-q[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(q, (-nums[i], i))
            # 只有堆顶元素不在窗口内时才将其移除
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans
