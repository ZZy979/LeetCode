# 官方题解2：二进制
# 时间复杂度O(nlog n)，空间复杂度O(1)
# 1832 ms
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        m = max_bit(n - 1)
        for b in range(m + 1):
            x = sum(1 for num in nums if num & (1 << b) != 0)
            y = sum(1 for num in range(1, n) if num & (1 << b) != 0)
            if x > y:
                ans |= 1 << b
        return ans


def max_bit(n):
    m = 31
    while (n >> m) == 0:
        m -= 1
    return m
