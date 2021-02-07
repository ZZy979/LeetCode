# 评论区解法：二分查找
# 时间复杂度O(klog k+k(n-k))，空间复杂度O(k)
# 76 ms
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        window = sorted(nums[:k])
        ans = [(window[k // 2] + window[(k - 1) // 2]) / 2]
        for i in range(k, n):
            window.insert(bisect_left(window, nums[i]), nums[i])
            window.pop(bisect_left(window, nums[i - k]))
            ans.append((window[k // 2] + window[(k - 1) // 2]) / 2)
        return ans
