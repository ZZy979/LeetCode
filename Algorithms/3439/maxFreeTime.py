# 滑动窗口，时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        startTime.append(eventTime)
        endTime.append(eventTime)
        window_time = sum(endTime[i] - startTime[i] for i in range(k))
        ans = startTime[k] - window_time
        for i in range(k, n):
            window_time += (endTime[i] - startTime[i]) - (endTime[i - k] - startTime[i - k])
            ans = max(ans, startTime[i + 1] - endTime[i - k] - window_time)
        return ans
