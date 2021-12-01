# 错误dp：不能用贪心算法
# ring = "caotmcaataijjxi", key = "oatjii"答案是18不是19
# 正确：o->第2或3个a->第2个t->第1个j->第1个i，错误：o->第1个a->第1个t->第2个j->第2个i
from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m, n = len(ring), len(key)
        positions = defaultdict(list)
        for i in range(m):
            positions[ring[i]].append(i)
        # dp[i]: 拼写key[0:i]需要的最小步数
        dp = [0] * n
        # rotate[i]: 拼写完key[0:i]后ring的旋转位置(0~m-1)
        rotate = [0] * n
        dp[0], rotate[0] = find_min(positions[key[0]], m, 0)
        for i in range(1, n):
            dp[i], rotate[i] = find_min(positions[key[i]], m, rotate[i - 1])
            dp[i] += dp[i - 1]
        return dp[-1] + n


def find_min(positions, m, r):
    min_step = 9999
    min_p = None
    for p in positions:
        rp = (p - r) % m
        step = min(rp, m - rp)
        if step < min_step:
            min_step = step
            min_p = p
    return min_step, min_p
