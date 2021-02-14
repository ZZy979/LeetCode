# 官方题解
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 1
        left = right = 0
        while right < n - 1:
            if left == right:
                if arr[left] == arr[left + 1]:
                    left += 1
                right += 1
            else:
                if arr[right] > arr[right - 1] and arr[right] > arr[right + 1] or arr[right] < arr[right - 1] and arr[right] < arr[right + 1]:
                    right += 1
                else:
                    left = right
            ans = max(ans, right - left + 1)
        return ans
