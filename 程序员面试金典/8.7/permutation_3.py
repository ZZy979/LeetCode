import itertools

# 方法3：使用标准库函数
# 60 ms
class Solution:
    def permutation(self, S: str) -> List[str]:
        return [''.join(p) for p in itertools.permutations(S)]
