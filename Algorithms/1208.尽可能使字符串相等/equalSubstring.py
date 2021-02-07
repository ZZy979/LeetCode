class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        left = right = 0
        c = ans = 0
        while right < n:
            c += cost[right]
            while c > maxCost:
                c -= cost[left]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans
