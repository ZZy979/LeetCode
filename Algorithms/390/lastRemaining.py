class Solution:
    def lastRemaining(self, n: int) -> int:
        # 删除次数K = n.bit_length() - 1
        # 第k次删除前数组长度n[k] = n >> k，k为偶数时从左到右，k为奇数时从右向左
        # k为偶数时a[k+1][i] = a[k][2i]，k为奇数时a[k+1][n[k+1]+1-i] = a[k][n[k]+1-2i], a[0][i]=i
        idx = 1
        for k in range(n.bit_length() - 2, -1, -1):
            if k % 2 == 0:
                idx *= 2
            else:
                # n[k+1]+1-i=idx => i=n[k+1]+1-idx => n[k]+1-2i=n[k]-2n[k+1]-1+2idx
                idx = (n >> k) - 2 * (n >> (k + 1)) - 1 + 2 * idx
        return idx
