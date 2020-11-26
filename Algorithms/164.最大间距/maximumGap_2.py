# 方法2：桶排序
# 时间复杂度：O(n)，空间复杂度：O(n)
# 44 ms
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        min_val, max_val = min(nums), max(nums)
        d = max(1, (max_val - min_val) // (n - 1))
        bucket_size = (max_val - min_val) // d + 1
        buckets = [[-1, -1] for _ in range(bucket_size)]
        for x in nums:
            idx = (x - min_val) // d
            if buckets[idx][0] == -1:
                buckets[idx][0] = buckets[idx][1] = x
            else:
                buckets[idx][0] = min(buckets[idx][0], x)
                buckets[idx][1] = max(buckets[idx][1], x)
        
        ans, prev = 0, -1
        for i in range(bucket_size):
            if buckets[i][0] == -1:
                continue
            if prev != -1:
                ans = max(ans, buckets[i][0] - buckets[prev][1])
            prev = i
        return ans
