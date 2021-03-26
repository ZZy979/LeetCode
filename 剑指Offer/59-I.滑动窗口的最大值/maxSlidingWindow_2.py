from collections import deque

# 方法2：单调队列
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        q = deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        ans = [nums[q[0]]]
        for i in range(k, len(nums)):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            if q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])
        return ans
