class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for x in range(len(arr), 0, -1):
            idx = arr.index(x, 0, x)
            if idx != x - 1:
                flip(arr, 0, idx)
                flip(arr, 0, x - 1)
                ans.append(idx + 1)
                ans.append(x)
        return ans


def flip(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
