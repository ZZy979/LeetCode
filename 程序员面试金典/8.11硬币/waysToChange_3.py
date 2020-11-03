# 方法3：数学法
# 64 ms
class Solution:
    def waysToChange(self, n: int) -> int:
        ans = 0
        for num in range(n // 25 + 1):
            rest = n - 25 * num
            a, b = rest // 10, rest % 10 // 5
            ans += (a + 1) * (a + b + 1)
            ans %= 1000000007
        return ans
