class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res, left, right = [0] * n, 0, n - 1
        for num in nums:
            if num % 2 == 0:
                res[left] = num
                left += 1
            else:
                res[right] = num
                right -= 1
        return res
