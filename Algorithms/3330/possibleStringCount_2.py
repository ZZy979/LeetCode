class Solution:
    def possibleStringCount(self, word: str) -> int:
        return sum(word[i] == word[i - 1] for i in range(1, len(word))) + 1
