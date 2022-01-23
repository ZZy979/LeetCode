class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # f[i]表示还剩下第i~n−1堆石子时，当前玩家比下一位玩家最多能多拿到的石子数目
        # 边界情况，当没有石子时，分数为 0
        f = [-10**9] * n + [0]
        for i in range(n - 1, -1, -1):
            pre = 0
            for j in range(i + 1, min(i + 3, n) + 1):
                pre += stoneValue[j - 1]
                f[i] = max(f[i], pre - f[j])
        return "Tie" if f[0] == 0 else "Alice" if f[0] > 0 else "Bob"
