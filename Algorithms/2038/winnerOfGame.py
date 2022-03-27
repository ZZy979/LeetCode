class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        move = {'A': 0, 'B': 0}
        count = {'A': 0, 'B': 0}
        for i in range(len(colors)):
            if i == 0 or colors[i] == colors[i - 1]:
                count[colors[i]] += 1
            else:
                move[colors[i - 1]] += max(0, count[colors[i - 1]] - 2)
                count[colors[i]] = 1
        move[colors[-1]] += max(0, count[colors[-1]] - 2)
        return move['A'] > move['B']
