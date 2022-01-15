class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m1, m2, idx = -1, -1, 0
        for i, x in enumerate(nums):
            if x > m1:
                m1, m2, idx = x, m1, i
            elif x > m2:
                m2 = x
        return idx if m1 >= 2 * m2 else -1
