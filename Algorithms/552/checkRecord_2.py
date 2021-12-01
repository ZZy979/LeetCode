# 评论区解法：动态规划
class Solution:
    def checkRecord(self, n: int) -> int:
        q = 10**9 + 7
        # aij: i个A，最后连续j个L
        a00, a01, a02, a10, a11, a12 = 1, 1, 0, 1, 0, 0
        for _ in range(n - 1):
            a00, a01, a02, a10, a11, a12 = (
                (a00 + a01 + a02) % q,  # P
                a00,  # L
                a01,  # L
                (a00 + a01 + a02 + a10 + a11 + a12),  # A或P
                a10,  # L
                a11  # L
            )
        return (a00 + a01 + a02 + a10 + a11 + a12) % q
