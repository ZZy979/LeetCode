class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = ''.join(sorted(str(n)))
        return any(s == ''.join(sorted(str(2 ** i))) for i in range(32))
