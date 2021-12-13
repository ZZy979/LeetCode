class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = ''.join(c for c in licensePlate.lower() if c.islower())
        return sorted((word for word in words if all(word.count(c) >= licensePlate.count(c) for c in licensePlate)), key=len)[0]
