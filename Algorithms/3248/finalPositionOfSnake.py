class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i = j = 0
        for cmd in commands:
            if cmd == 'UP':
                i -= 1
            elif cmd == 'DOWN':
                i += 1
            elif cmd == 'LEFT':
                j -= 1
            elif cmd == 'RIGHT':
                j += 1
        return i * n + j
