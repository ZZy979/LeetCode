class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = 0x7fffffff
        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                return True
        return False
