class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if changed:
                    return False
                else:
                    if i > 0 and nums[i + 1] < nums[i - 1]:
                        nums[i + 1] = nums[i]
                    changed = True
        return True
