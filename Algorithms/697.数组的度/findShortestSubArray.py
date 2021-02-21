from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        degree = count.most_common(1)[0][1]
        max_freq_nums = {x for x in count if count[x] == degree}
        first_idx, last_idx = {}, {}
        for i, x in enumerate(nums):
            if x in max_freq_nums:
                if x not in first_idx:
                    first_idx[x] = i
                last_idx[x] = i
        
        ans = 99999
        for x in max_freq_nums:
            ans = min(ans, last_idx[x] - first_idx[x] + 1)
            if ans == degree:
                break
        return ans
