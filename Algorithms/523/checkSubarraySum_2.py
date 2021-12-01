class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = 0
        m = {0: -1}
        for i, x in enumerate(nums):
            remainder = (remainder + x) % k
            if remainder in m:
                if i - m[remainder] >= 2:
                    return True
            else:
                m[remainder] = i
        return False
