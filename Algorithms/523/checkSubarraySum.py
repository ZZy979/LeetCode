class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre = 0
        mod = {0: {0}}
        for i, x in enumerate(nums):
            pre += x
            if pre % k in mod and any(i + 1 - j >= 2 for j in mod[pre % k]):
                return True
            mod.setdefault(pre % k, set()).add(i + 1)
        return False
