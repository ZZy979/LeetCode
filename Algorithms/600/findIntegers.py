class Solution:
    def __init__(self):
        self.dp = [0] * 32
        self.dp[1], self.dp[2] = 2, 3
        for i in range(3, 32):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]

    def findIntegers(self, n: int) -> int:
        if n <= 2:
            return n + 1
        elif n == 3:
            return 3
        b = n.bit_length()
        # 2^(b-1) <= n < 2^b-1
        if n < 3 * 2**(b - 2):
            return self.dp[b - 1] + self.findIntegers(n - 2**(b - 1))
        else:
            return self.dp[b]
