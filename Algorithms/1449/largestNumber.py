from collections import Counter

# 元素是字典的动态规划，最后一个用例超时
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [Counter() for _ in range(target + 1)]
        for i in range(1, 10):
            for j in range(cost[i - 1], target + 1):
                if cost[i - 1] == j or cost[i - 1] < j and dp[j - cost[i - 1]]:
                    m = counter2num(dp[j])
                    c = dp[j - cost[i - 1]].copy()
                    c[i] += 1
                    n = counter2num(c)
                    if cmp(n, m) > 0:
                        dp[j] = c
        return counter2num(dp[-1]) or '0'


def counter2num(c):
    return ''.join(map(str, sorted(c.elements(), reverse=True)))


def cmp(s1, s2):
    if len(s1) != len(s2):
        return len(s1) - len(s2)
    elif s1 != s2:
        return -1 if s1 < s2 else 1
    else:
        return 0
