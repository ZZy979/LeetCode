import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.flipped = set()

    def flip(self) -> List[int]:
        i = random.randrange(self.m * self.n)
        while i in self.flipped:
            i = random.randrange(self.m * self.n)
        self.flipped.add(i)
        return divmod(i, self.n)

    def reset(self) -> None:
        self.flipped.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
