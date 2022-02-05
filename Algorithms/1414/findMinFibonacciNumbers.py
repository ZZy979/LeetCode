import bisect

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibonacci = []
        a, b = 1, 1
        while a <= k:
            fibonacci.append(a)
            a, b = b, a + b
        
        ans = 0
        while k > 0:
            k -= fibonacci[bisect.bisect_right(fibonacci, k) - 1]
            ans += 1
        return ans
