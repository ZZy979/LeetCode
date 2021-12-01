import bisect

# 评论区解法：二分查找+插入，时间复杂度O(n²)
# 1680 ms
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        q = []
        ans = 0
        for x in nums:
            i = bisect.bisect_left(q, -x)
            ans += i
            q.insert(i, -x)
        return ans
