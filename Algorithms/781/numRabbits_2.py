from collections import Counter

# 官方题解：如果有x只兔子回答y，则至少有ceil(x/(y+1))*(y+1)只
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = sum((x + y) // (y + 1) * (y + 1) for y, x in count.items())
        return ans
