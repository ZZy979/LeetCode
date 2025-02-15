from collections import Counter

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = Counter(map(box, range(lowLimit, highLimit + 1)))
        return boxes.most_common(1)[0][1]

def box(ball):
    return sum(map(int, str(ball)))
