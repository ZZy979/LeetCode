class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        last_idx = [-1] * 26
        for i in range(n):
            last_idx[ord(s[i]) - ord('a')] = i

        t, ans = [], []
        cur = 0
        for i in range(len(last_idx)):
            c = chr(ord('a') + i)
            while t and t[-1] <= c:
                ans.append(t.pop())
            while cur <= last_idx[i]:
                if s[cur] == c:
                    ans.append(c)
                else:
                    t.append(s[cur])
                cur += 1
        return ''.join(ans + t[::-1])
