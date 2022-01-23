class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0] * 3
        for s in stones:
            count[s % 3] += 1
        if count[0] % 2 == 0:
            return count[1] != 0 and count[2] != 0
        else:
            return count[2] > count[1] + 2 or count[1] > count[2] + 2
