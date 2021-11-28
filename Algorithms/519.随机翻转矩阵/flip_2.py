import random

# 官方题解
class Solution:

    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.total = m * n
        self.map = {}

    def flip(self) -> List[int]:
        x = random.randrange(self.total)
        self.total -= 1
        idx = self.map.get(x, x)
        self.map[x] = self.map.get(self.total, self.total)
        return divmod(idx, self.n)

    def reset(self) -> None:
        self.total = self.m * self.n
        self.map.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
