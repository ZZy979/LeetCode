from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        res = []
        while cnt:
            res.append(list(cnt))
            for x in res[-1]:
                cnt[x] -= 1
                if cnt[x] == 0:
                    del cnt[x]
        return res
