class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        code = self.grayCode(n - 1)
        return code + [x + (1 << (n - 1)) for x in reversed(code)]
