class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        return sorted(((releaseTimes[0] if i == 0 else releaseTimes[i] - releaseTimes[i - 1], keysPressed[i]) for i in range(len(releaseTimes))), reverse=True)[0][1]
