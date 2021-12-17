class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            k, r = divmod(numBottles, numExchange)
            ans += k
            numBottles = k + r
        return ans
