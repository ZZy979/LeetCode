# 方法1：由S[1:n]的排列组合构造S的排列组合（S[0]插空）
# 100 ms
class Solution:
    def permutation(self, S: str) -> List[str]:
        return [''.join(p) for p in permutations(S)]


def permutations(s):
    return [[]] if not s else [p[:i] + [s[0]] + p[i:] for p in permutations(s[1:]) for i in range(len(p) + 1)]
