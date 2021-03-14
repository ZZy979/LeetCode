class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        n = nums.count(0)
        last = nums[n]
        i = n + 1
        while i < 5:
            if nums[i] == last + 1:
                last = nums[i]
                i += 1
            elif n > 0:
                last += 1
                n -= 1
            else:
                return False
        return True
