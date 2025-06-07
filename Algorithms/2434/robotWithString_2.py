# 官方题解：贪心+栈，时间复杂度O(n+C)，空间复杂度O(n)，其中C=26
class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = Counter(s)
        stack = []
        res = []
        minCharacter = 'a'
        for c in s:
            stack.append(c)
            cnt[c] -= 1
            while minCharacter != 'z' and cnt[minCharacter] == 0:
                minCharacter = chr(ord(minCharacter) + 1)
            while stack and stack[-1] <= minCharacter:
                res.append(stack.pop())
        return ''.join(res)
