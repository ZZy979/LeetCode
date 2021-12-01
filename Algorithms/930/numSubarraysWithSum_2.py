# 官方题解1：枚举子数组中1的位置
# 时间复杂度O(n)，空间复杂度O(n)
# 252 ms
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        indices = [-1] + [i for i, v in enumerate(A) if v] + [len(A)]
        ans = 0
        if S == 0:
            for i in range(len(indices) - 1):
                # w: number of zeros between two consecutive ones
                w = indices[i + 1] - indices[i] - 1
                ans += w * (w + 1) // 2
            return ans
        for i in range(1, len(indices) - S):
            j = i + S - 1
            left = indices[i] - indices[i - 1]
            right = indices[j + 1] - indices[j]
            ans += left * right
        return ans
