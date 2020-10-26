class Solution:
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        n = w // 32
        h = length // n
        screen = [0] * length
        c1, b1 = divmod(x1, 32)
        c2, b2 = divmod(x2, 32)
        if c1 == c2:
            screen[y * n + c1] |= ((1 << (b2 - b1 + 1)) - 1) << (31 - b2)
        else:
            screen[y * n + c1] |= (1 << (32 - b1)) - 1
            for c in range(c1 + 1, c2):
                screen[y * n + c] = -1
            screen[y * n + c2] |= -1 << (31 - b2)
        return screen
