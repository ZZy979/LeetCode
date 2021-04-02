class Solution:
    def clumsy(self, N: int) -> int:
        tmp = []
        last = (0, 1, 2, 6)
        for i in range(N, 3, -4):
            tmp.append(i * (i - 1) // (i - 2))
            tmp.append(i - 3)
        tmp.append(last[N % 4])
        return tmp[0] + sum(tmp[1::2]) - sum(tmp[2::2])
