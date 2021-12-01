# 官方题解：动态规划
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        # x 的范围为 [0, 2^10)
        MAXX = 2**10
        
        n = len(nums)
        f = [float("inf")] * MAXX
        # 边界条件 f(-1,0)=0
        f[0] = 0
        
        for i in range(k):
            # 第 i 个组的哈希映射
            count = Counter()
            size = 0
            for j in range(i, n, k):
                count[nums[j]] += 1
                size += 1

            # 求出 t2
            t2min = min(f)

            g = [t2min] * MAXX
            for mask in range(MAXX):
                # t1 则需要枚举 x 才能求出
                for x, countx in count.items():
                    g[mask] = min(g[mask], f[mask ^ x] - countx)
            
            # 别忘了加上 size
            f = [val + size for val in g]

        return f[0]
