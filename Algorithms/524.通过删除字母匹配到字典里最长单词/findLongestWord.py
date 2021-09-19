class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary = sorted(sorted(dictionary), key=len, reverse=True)
        for w in dictionary:
            if is_subsequence(w, s):
                return w
        return ''


def is_subsequence(a, b):
    if len(b) < len(a):
        return False
    i = 0
    for c in a:
        while i < len(b) and b[i] != c:
            i += 1
        if i >= len(b):
            return False
        i += 1
    return True
