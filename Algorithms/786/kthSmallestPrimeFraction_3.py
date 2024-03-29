# 官方题解3：二分查找+双指针
# 时间复杂度O(nlog C)，C是数组中元素的上界，空间复杂度O(1)
# 60 ms
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        left, right = 0.0, 1.0
        while True:
            mid = (left + right) / 2
            i, count = -1, 0
            x, y = 0, 1

            for j in range(1, len(arr)):
                while arr[i + 1] / arr[j] < mid:
                    i += 1
                    if arr[i] * y > arr[j] * x:
                        x, y = arr[i], arr[j]
                count += i + 1
            if count == k:
                return [x, y]
            elif count < k:
                left = mid
            else:
                right = mid
