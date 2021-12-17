class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)
        ans = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                x, y, length = arr[i], arr[j], 1
                while y in s:
                    x, y = y, x + y
                    length += 1
                ans = max(ans, length)
        return ans if ans >= 3 else 0
