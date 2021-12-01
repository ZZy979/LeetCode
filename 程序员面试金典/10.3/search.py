class Solution:
    def search(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            if arr[left] == target:
                return left
            mid = (left + right) // 2
            if arr[mid] == target:
                right = mid
            elif arr[mid] > arr[right]:
                if arr[left] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[mid] < arr[right]:
                if arr[mid] < target <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                right -= 1
        return -1
