class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = i = x = 0
        while (j := index(nums, x, i)) != -1:
            ans += 1
            x = 1 - x
            i = j
        return ans

def index(seq, value, start):
    while start < len(seq) and seq[start] != value:
        start += 1
    return -1 if start == len(seq) else start
