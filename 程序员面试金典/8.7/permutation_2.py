# 方法2：由S的所有长度为n-1的子序列的排列组合构造S的排列组合（在开头固定每一个字符）
# 280 ms
class Solution:
    def permutation(self, S: str) -> List[str]:
        return [''.join(p) for p in permutaions(list(S), 0)]


def permutaions(a, k):
    if k == len(a) - 1:
        yield [a[k]]
    else:
        for i in range(k, len(a)):
            a[i], a[k] = a[k], a[i]
            for p in permutaions(a, k + 1):
                yield [a[k]] + p
            a[i], a[k] = a[k], a[i]
