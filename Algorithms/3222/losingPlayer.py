class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        return 'Alice' if min(x, y // 4) % 2 == 1 else 'Bob'
