from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        count = Counter(hand)
        for x in hand:
            if count[x] == 0:
                continue
            for y in range(x, x + groupSize):
                if count[y] == 0:
                    return False
                count[y] -= 1
        return True
