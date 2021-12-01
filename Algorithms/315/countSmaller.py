import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        queue = []
        res = []
        for i in range(len(nums) - 1, -1, -1):
            loc = bisect.bisect_left(queue, nums[i])
            res.append(loc)
            queue.insert(loc, nums[i])
        return res[::-1]
