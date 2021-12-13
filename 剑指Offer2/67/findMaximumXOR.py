class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        x = 0
        for k in range(30, -1, -1):
            seen = {num >> k for num in nums}
            x_next = x * 2 + 1
            if any(x_next ^ (num >> k) in seen for num in nums):
                x = x_next
            else:
                x = x_next - 1
        return x
