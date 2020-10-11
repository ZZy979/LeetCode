class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxs = [-4294967296] * 3
        for num in nums:
            if num > maxs[0]:
                maxs = [num, maxs[0], maxs[1]]
            elif num != maxs[0] and num > maxs[1]:
                maxs[2] = maxs[1]
                maxs[1] = num
            elif num != maxs[0] and num != maxs[1] and num > maxs[2]:
                maxs[2] = num
        return maxs[0] if maxs[2] == -4294967296 else maxs[2]
