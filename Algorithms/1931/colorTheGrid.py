# 官方题解：状态压缩动态规划，时间复杂度O(3^(2m)*n)，空间复杂度O(3^(2m))
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9 + 7
        # 哈希映射 valid 存储所有满足要求的对一行进行涂色的方案
        # 键表示 mask，值表示 mask 的三进制串（以列表的形式存储）
        valid = {}

        # 在 [0, 3^m) 范围内枚举满足要求的 mask
        for mask in range(3**m):
            color = []
            mm = mask
            for i in range(m):
                color.append(mm % 3)
                mm //= 3
            if any(color[i] == color[i + 1] for i in range(m - 1)):
                continue
            valid[mask] = color

        # 预处理所有的 (mask1, mask2) 二元组，满足 mask1 和 mask2 作为相邻行时，同一列上两个格子的颜色不同
        adjacent = defaultdict(list)
        for mask1, color1 in valid.items():
            for mask2, color2 in valid.items():
                if not any(x == y for x, y in zip(color1, color2)):
                    adjacent[mask1].append(mask2)

        f = [int(mask in valid) for mask in range(3**m)]
        for i in range(1, n):
            g = [0] * (3**m)
            for mask2 in valid:
                for mask1 in adjacent[mask2]:
                    g[mask2] = (g[mask2] + f[mask1]) % mod
            f = g
        return sum(f) % mod
