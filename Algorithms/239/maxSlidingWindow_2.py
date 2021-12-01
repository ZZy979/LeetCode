# 官方题解2：单调队列
# 时间复杂度O(n)，空间复杂度O(k)
# 336 ms
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
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
