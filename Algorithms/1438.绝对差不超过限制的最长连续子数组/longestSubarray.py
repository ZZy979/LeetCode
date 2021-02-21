from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q, min_q = deque(), deque()
        left = ans = 0
        for right in range(len(nums)):
            while max_q and max_q[-1] < nums[right]:
                max_q.pop()
            max_q.append(nums[right])
            while min_q and min_q[-1] > nums[right]:
                min_q.pop()
            min_q.append(nums[right])

            while max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[left]:
                    max_q.popleft()
                if min_q[0] == nums[left]:
                    min_q.popleft()
                left += 1
            ans = max(ans, right - left + 1)
        return ans
