from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for n in count:
            while count[n] >= n + 1:
               ans += n + 1
               count[n] -= n + 1
            if count[n] > 0:
                ans += n + 1
        return ans
 