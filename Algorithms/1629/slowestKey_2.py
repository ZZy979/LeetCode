class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        return max(zip(map(int.__sub__, releaseTimes, [0] + releaseTimes), keysPressed))[1]
