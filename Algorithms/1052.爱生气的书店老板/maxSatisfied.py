class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        satisfied = ans = sum(customers[:X]) + sum(customers[i] for i in range(X, n) if grumpy[i] == 0)
        for i in range(X, n):
            if grumpy[i] == 1:
                satisfied += customers[i]
            if grumpy[i - X] == 1:
                satisfied -= customers[i - X]
            ans = max(ans, satisfied)
        return ans
