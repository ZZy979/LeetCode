class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        a = sorted(((x, i) for i, x in enumerate(nums)), reverse=True)
        return a[0][1] if len(a) < 2 or a[0][0] >= 2 * a[1][0] else -1
