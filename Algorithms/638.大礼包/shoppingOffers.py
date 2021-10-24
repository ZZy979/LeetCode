# 回溯
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.ans = 0x7fffffff
        self.backtrack(price, special, needs, 0, 0)
        return self.ans
    
    def backtrack(self, price, special, needs, start, cost):
        if start >= len(special):
            cost += sum(p * n for p, n in zip(price, needs))
            self.ans = min(self.ans, cost)
            return
        for i in range(start, len(special) + 1):
            if i == len(special):
                self.backtrack(price, special, needs, i, cost)
            elif all(m <= n for m, n in zip(special[i], needs)):
                for j in range(len(needs)):
                    needs[j] -= special[i][j]
                self.backtrack(price, special, needs, i, cost + special[i][-1])
                for j in range(len(needs)):
                    needs[j] += special[i][j]
