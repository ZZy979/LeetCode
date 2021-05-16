# 官方题解1：哈希表
# 时间复杂度O(nlog C)，空间复杂度O(n)
# 272 ms
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        x = 0
        for k in range(30, -1, -1):
            seen = {num >> k for num in nums}
            x_next = x * 2 + 1
            found = False
            for num in nums:
                if x_next ^ (num >> k) in seen:
                    found = True
                    break
            if found:
                x = x_next
            else:
                x = x_next - 1
        return x
