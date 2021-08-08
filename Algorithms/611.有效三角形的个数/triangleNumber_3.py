# 评论区解法
# 804 ms
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums) - 1, 1, -1):
            j, k = 0, i - 1
            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    ans += k - j
                    k -= 1
                else:
                    j += 1
        return ans
