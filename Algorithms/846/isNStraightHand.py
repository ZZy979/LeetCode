from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        for _ in range(len(hand) // groupSize):
            x = min(count)
            count[x] -= 1
            if count[x] == 0:
                del count[x]
            for y in range(x + 1, x + groupSize):
                if count[y] == 0:
                    return False
                count[y] -= 1
                if count[y] == 0:
                    del count[y]
        return True
