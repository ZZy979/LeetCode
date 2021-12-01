class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        left, ans = 0, 1
        less = None
        for right in range(1, len(arr)):
            if arr[right] == arr[right - 1]:
                left = right
                continue
            if right > left + 1 and (arr[right] < arr[right - 1]) == less:
                left = right - 1
            less = arr[right] < arr[right - 1]
            ans = max(ans, right - left + 1)
        return ans
