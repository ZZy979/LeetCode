class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0
        minutes = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        return min(min(minutes[i + 1] - minutes[i] for i in range(len(minutes) - 1)), minutes[0] + 1440 - minutes[-1])
