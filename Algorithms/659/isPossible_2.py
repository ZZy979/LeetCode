from collections import Counter

# 官方题解2：贪心
# 时间复杂度O(n)，空间复杂度O(n)
# 104 ms
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        countMap = Counter(nums)
        endMap = Counter()
        for x in nums:
            if countMap[x] > 0:
                if endMap[x - 1] > 0:
                    countMap[x] -= 1
                    endMap[x - 1] -= 1
                    endMap[x] += 1
                else:
                    if countMap[x + 1] > 0 and countMap[x + 2] > 0:
                        countMap[x] -= 1
                        countMap[x + 1] -= 1
                        countMap[x + 2] -= 1
                        endMap[x + 2] += 1
                    else:
                        return False
        
        return True
