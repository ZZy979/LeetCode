class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = []
        while n:
            n, m = divmod(n - 1, 26)
            ans.append(chr(ord('A') + m))
        return ''.join(reversed(ans))
