class Solution:
    def search(self, arr: List[int], target: int) -> int:
        if not arr:
            return -1
        left, right = 0, len(arr) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                right = mid - 1
                if ans == -1 or ans > mid:
                    ans = mid
            elif arr[mid] > arr[right]:
                if arr[left] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[mid] < arr[right]:
                if target < arr[mid] or target > arr[right] or arr[left] == target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right -= 1
        return ans
