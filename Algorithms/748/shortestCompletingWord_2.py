from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = Counter(filter(str.isalpha, licensePlate.lower()))
        return min(filter(lambda word: not (licensePlate - Counter(word.lower())), words), key=len)
