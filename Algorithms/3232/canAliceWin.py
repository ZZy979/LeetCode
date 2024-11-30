class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        return sum(x for x in nums if x < 10) != sum(x for x in nums if x >= 10)
