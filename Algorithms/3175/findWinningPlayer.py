from collections import deque

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        k = min(k, n)
        q = deque(range(n))
        win = 0
        while True:
            if skills[q[0]] > skills[q[1]]:
                winner, loser = q[0], q[1]
                q[0], q[1] = q[1], q[0]
                win += 1
            else:
                winner, loser = q[1], q[0]
                win = 1
            if win >= k:
                return winner
            q.append(q.popleft())
