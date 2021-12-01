class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        return sum(min(timeSeries[i + 1] - timeSeries[i], duration) for i in range(len(timeSeries) - 1)) + duration
