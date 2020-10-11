class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        reverse = {word[::-1]: i for i, word in enumerate(words)}
        ans = []
        for i, word in enumerate(words):
            for k in range(len(word) + 1):
                pref, suf = word[:k], word[k:]
                if suf[::-1] == suf:
                    j = reverse.get(pref)
                    if j is not None and j != i:
                        ans.append((i, j))
                if k and pref[::-1] == pref:
                    j = reverse.get(suf)
                    if j is not None and j != i:
                        ans.append((j, i))
        return ans
