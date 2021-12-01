class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mp = {}
        for i, num in enumerate(nums):
            if num in mp:
                mp[num][0] += 1
                mp[num][2] = i
            else:
                mp[num] = [1, i, i]
        
        maxNum = minLen = 0
        for count, left, right in mp.values():
            if maxNum < count:
                maxNum = count
                minLen = right - left + 1
            elif maxNum == count:
                if minLen > (span := right - left + 1):
                    minLen = span
        return minLen
