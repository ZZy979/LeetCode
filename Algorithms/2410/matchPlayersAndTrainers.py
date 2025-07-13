# 排序+双指针，时间复杂度O(mlog m + nlog n)，空间复杂度O(log m + log n)
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        j = len(trainers) - 1
        ans = 0
        for i in range(len(players) - 1, -1, -1):
            if j >= 0 and players[i] <= trainers[j]:
                ans += 1
                j -= 1
        return ans
