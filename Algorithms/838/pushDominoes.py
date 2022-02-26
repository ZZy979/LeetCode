from collections import deque

# 个人方法
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        q = deque([(i, d) for i, d in enumerate(dominoes) if d in 'LR'])
        while q:
            for i in range(len(q)):
                dominoes[q[i][0]] = q[i][1]
            for _ in range(len(q)):
                i, _ = q.popleft()
                if dominoes[i] == 'L':
                    if i >= 1 and dominoes[i - 1] == '.' and (i == 1 or i > 1 and dominoes[i - 2] != 'R'):
                        q.append((i - 1, 'L'))
                elif dominoes[i] == 'R':
                    if i < len(dominoes) - 1 and dominoes[i + 1] == '.' and (i == len(dominoes) - 2 or i < len(dominoes) - 2 and dominoes[i + 2] != 'L'):
                        q.append((i + 1, 'R'))
        return ''.join(dominoes)
