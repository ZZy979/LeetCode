# https://leetcode.cn/problems/minimum-number-of-swaps-to-make-the-string-balanced/solutions/922728/go-tan-xin-by-endlesscheng-7h9n/
class Solution:
    def minSwaps(self, s: str) -> int:
        c = 0
        for b in s:
            if b == '[' or c == 0:
                c += 1
            else:
                c -= 1
        return c // 2
