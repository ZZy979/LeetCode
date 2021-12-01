class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        return reduce(xor, nums) == 0
