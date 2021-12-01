from collections import defaultdict

# 个人方法，枚举每一块石头跳过来的步数，计算可达性
# 264 ms
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        n = len(stones)
        reachable = {s: False for s in stones}
        reachable[0] = reachable[1] = True
        steps = defaultdict(set)
        steps[1] = {1}
        for i in range(1, n):
            s = stones[i]
            if reachable[s]:
                for k in steps[s]:
                    for nk in (k - 1, k, k + 1):
                        if nk > 0 and s + nk in reachable:
                            reachable[s + nk] = True
                            steps[s + nk].add(nk)
        return reachable[stones[-1]]
