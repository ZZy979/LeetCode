# 官方题解：栈+贪心，时间复杂度O(nC)，空间复杂度O(n+C)，其中C=26
class Solution:
    def clearStars(self, s: str) -> str:
        cnt = [[] for _ in range(26)]
        arr = list(s)
        for i, c in enumerate(arr):
            if c != '*':
                cnt[ord(c) - ord('a')].append(i)
            else:
                for j in range(26):
                    if cnt[j]:
                        arr[cnt[j].pop()] = '*'
                        break
        return ''.join(c for c in arr if c != '*')
