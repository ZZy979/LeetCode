class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if (i := word.find(ch)) != -1:
            return word[i::-1] + word[i + 1:]
        return word
