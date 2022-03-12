# 官方题解：差分数组
# 时间复杂度O(n)，空间复杂度O(n)
# 252 ms
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diffs = [0] * n
        for i, num in enumerate(nums):
            low = (i + 1) % n
            high = (i - num + n + 1) % n
            diffs[low] += 1
            diffs[high] -= 1
            if low >= high:
                diffs[0] += 1
        score, maxScore, idx = 0, 0, 0
        for i, diff in enumerate(diffs):
            score += diff
            if score > maxScore:
                maxScore, idx = score, i
        return idx
