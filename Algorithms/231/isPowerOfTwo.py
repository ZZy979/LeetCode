class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            n, r = divmod(n, 2)
            if r != 0:
                return False
        return True
