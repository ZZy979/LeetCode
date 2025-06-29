# https://leetcode.cn/problems/longest-subsequence-repeated-k-times/solutions/1006067/mei-ju-pai-lie-zi-xu-lie-pi-pei-by-endle-oi2h/
# 枚举排列+判断子序列，时间复杂度O((n/k)!*n)，空间复杂度O(nC)，其中C=26
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        cnt = Counter(s)
        a = [ch for ch, freq in cnt.items() for _ in range(freq // k)]
        a.sort(reverse=True)  # 排序后，下面会按照字典序从大到小枚举排列

        for i in range(len(a), 0, -1):  # 长的优先
            for perm in permutations(a, i):  # 枚举 a 的长为 i 的排列
                seq = ''.join(perm)
                if isSubsequence(seq * k, s):
                    return seq
        return ''

# 返回 seq 是否为 s 的子序列
def isSubsequence(seq, s):
    it = iter(s)
    return all(c in it for c in seq)  # in 会消耗迭代器
