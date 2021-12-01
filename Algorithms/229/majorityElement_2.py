# 官方题解2：摩尔投票法，时间复杂度O(n)，空间复杂度O(1)
# 56 ms
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element1 = element2 = 0
        vote1 = vote2 = 0
        for x in nums:
            if (vote1 == 0 or x == element1) and x != element2:
                element1 = x
                vote1 += 1
            elif vote2 == 0 or x == element2:
                element2 = x
                vote2 += 1
            else:
                vote1 -= 1
                vote2 -= 1
        
        ans = []
        if vote1 > 0 and nums.count(element1) > len(nums) // 3:
            ans.append(element1)
        if vote2 > 0 and nums.count(element2) > len(nums) // 3:
            ans.append(element2)
        return ans
