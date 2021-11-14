import bisect

class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        # 设k位数i的起始位置是b[i]
        # b[i] = b[10^(k-1)] + k * (i - 10^(k-1))
        # b[10^k] = b[10^(k-1)] + k * 9 * 10^(k-1)
        # f[k] = b[10^k]
        f, i = [1], 1
        for k in range(1, 10):
            f.append(f[-1] + 9 * i * k)
            i *= 10
        
        # 第n位落在数字i内部，i <= 10^k, b[i] <= n < b[i + 1]
        k = bisect.bisect(f, n)
        i = 10**(k - 1) + (n - f[k - 1]) // k
        b = f[k - 1] + k * (i - 10**(k - 1))
        return int(str(i)[n - b])
