# 官方题解：记忆化搜索
class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        q = 10**9 + 7
        requirements = {0: 0} | {end: cnt for (end, cnt) in requirements}
        if requirements[0] != 0:
            return 0
        
        # 逆序对为cnt且满足requirements的排列perm[0..end]的个数
        @cache
        def dfs(end, cnt):
            if end == 0:
                return 1
            if end - 1 in requirements:
                r = requirements[end - 1]
                if r <= cnt <= end + r:
                    return dfs(end - 1, r)
                else:
                    return 0
            else:
                res = 0
                for i in range(min(end, cnt) + 1):
                    res = (res + dfs(end - 1, cnt - i)) % q
                return res

        return dfs(n - 1, requirements[n - 1])
