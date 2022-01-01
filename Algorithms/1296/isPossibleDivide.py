from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        nums.sort()
        count = Counter(nums)
        for x in nums:
            if count[x] == 0:
                continue
            for y in range(x, x + k):
                if count[y] == 0:
                    return False
                count[y] -= 1
        return True
