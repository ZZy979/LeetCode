# 官方题解：折半搜索
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        left, cnt, ans = 1, 0, 0
        while cnt < n:
            right = left * 10
            # op = 0 表示枚举奇数长度回文，op = 1 表示枚举偶数长度回文
            for op in [0, 1]:
                # 枚举m位十进制数[10^m, 10^(m+1))
                for i in range(left, right):
                    if cnt == n:
                        break
                    s = str(i)
                    combined = int(s + (s[::-1] if op == 1 else s[-2::-1]))
                    if is_palindrome(combined, k):
                        cnt += 1
                        ans += combined
            left = right
        return ans

def is_palindrome(x, k):
    digits = []
    while x:
        digits.append(x % k)
        x //= k
    return digits == digits[::-1]
