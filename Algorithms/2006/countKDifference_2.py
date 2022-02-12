class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        count = Counter()
        for num in nums:
            ans += count[num + k] + count[num - k]
            count[num] += 1
        return ans
