class Solution:
    def kthCharacter(self, k: int) -> str:
        s = [0]
        while (n := len(s)) < k:
            s.extend((s[i] + 1) % 26 for i in range(n))
        return chr(ord('a') + s[k - 1])
