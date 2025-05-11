# 官方题解：记忆化搜索
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        num = list(map(int, num))
        tot = sum(num)
        if tot % 2 != 0:
            return 0
        target = tot // 2
        cnt = Counter(num)
        n = len(num)
        maxOdd = (n + 1) // 2
        psum = [0] * 11
        for i in range(9, -1, -1):
            psum[i] = psum[i + 1] + cnt[i]

        @cache
        def dfs(pos, curr, oddCnt):
            # 如果剩余的位置无法完成合法的放置，或者当前奇数位置的元素和大于目标值
            if oddCnt < 0 or psum[pos] < oddCnt or curr > target:
                return 0
            if pos > 9:
                return int(curr == target and oddCnt == 0)
            evenCnt = psum[pos] - oddCnt # 偶数位剩余需要填充的位数
            res = 0
            for i in range(max(0, cnt[pos] - evenCnt), min(cnt[pos], oddCnt) + 1):
                # 当前数字在奇数位放置 i 个，偶数位放置 cnt[pos] - i 个
                ways = comb(oddCnt, i) * comb(evenCnt, cnt[pos] - i) % MOD
                res += ways * dfs(pos + 1, curr + i * pos, oddCnt - i)
            return res % MOD

        return dfs(0, 0, maxOdd)
