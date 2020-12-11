from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant.popleft() + n)
                dire.popleft()
            else:
                radiant.popleft()
                dire.append(dire.popleft() + n)
        return 'Radiant' if radiant else 'Dire'
