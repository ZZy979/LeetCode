class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        return sum((hours[i] + hours[j]) % 24 == 0 for i in range(len(hours) - 1) for j in range(i + 1, len(hours)))
