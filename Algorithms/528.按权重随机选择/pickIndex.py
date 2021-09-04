class Solution:

    def __init__(self, w: List[int]):
        self.cum_weights = list(accumulate(w))

    def pickIndex(self) -> int:
        p = random.randrange(self.cum_weights[-1])
        left, right = 0, len(self.cum_weights)
        while left < right:
            mid = (left + right) // 2
            if p < self.cum_weights[mid]:
                right = mid
            else:
                left = mid + 1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
