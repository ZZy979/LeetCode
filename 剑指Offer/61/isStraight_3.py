# 官方题解2：排序+遍历
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        joker = 0
        nums.sort()
        for i in range(4):
            if nums[i] == 0:
                joker += 1
            elif nums[i] == nums[i + 1]:
                return False
        return nums[4] - nums[joker] < 5
