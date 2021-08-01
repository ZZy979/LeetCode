import math

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = int(math.log2(label))
        if level % 2 == 1:
            label = 3 * 2**level - 1 - label

        path = []
        while label >= 1:
            path.append(label)
            label //= 2
        path.reverse()

        for i in range(1, level + 1, 2):
            path[i] = 3 * 2**i - 1 - path[i]
        return path
