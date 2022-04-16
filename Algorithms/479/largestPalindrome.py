class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10 ** n - 1
        for left in range(upper, upper // 10, -1):
            p = int(str(left) + str(left)[::-1])
            x = upper
            while x * x >= p:
                if p % x == 0:
                    return p % 1337
                x -= 1
