class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        diff = 0
        for i in range(1, len(colors) - 1):
            if (s := colors[i - 1:i + 2]) == 'AAA':
                diff += 1
            elif s == 'BBB':
                diff -= 1
        return diff > 0
