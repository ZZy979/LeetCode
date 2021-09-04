class Solution:

    def __init__(self, w: List[int]):
        self.cum_weights = list(accumulate(w))

    def pickIndex(self) -> int:
        return bisect_left(self.cum_weights, random.randint(1, self.cum_weights[-1]))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
