class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return any(arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1 for i in range(len(arr) - 2))
