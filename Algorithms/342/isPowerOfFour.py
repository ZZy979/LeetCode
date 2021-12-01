import math

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and 4 ** int(math.log(num, 4)) == num
