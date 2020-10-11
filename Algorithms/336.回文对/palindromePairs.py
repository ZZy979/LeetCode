class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        reverse = {word[::-1]: i for i, word in enumerate(words)}
        ans = []
        for i, word in enumerate(words):
            for k in range(len(word) + 1):
                if self.is_palindrome(word[k:]):
                    j = reverse.get(word[:k])
                    if j is not None and j != i:
                        ans.append((i, j))
                if k and self.is_palindrome(word[:k]):
                    j = reverse.get(word[k:])
                    if j is not None and j != i:
                        ans.append((j, i))
        return ans

    def is_palindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True
