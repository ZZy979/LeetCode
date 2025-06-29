# 官方题解：贪心，时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        sm = cnt = 0
        bits = k.bit_length()
        for i, ch in enumerate(reversed(s)):
            if ch == '1':
                if i < bits and sm + (1 << i) <= k:
                    sm += 1 << i
                    cnt += 1
            else:
                cnt += 1
        return cnt
