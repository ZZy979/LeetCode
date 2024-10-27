# 双指针
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        i, j = 0, 1
        win = 0
        while j < len(skills) and win < k:
            if skills[i] < skills[j]:
                i = j
                win = 1
            else:
                win += 1
            j += 1
        return i
