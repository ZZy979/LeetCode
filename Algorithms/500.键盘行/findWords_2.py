# 官方题解
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row = '12210111011122000010020202'
        ans = []
        for word in words:
            r = row[ord(word[0].lower()) - ord('a')]
            if all(row[ord(c.lower()) - ord('a')] == r for c in word):
                ans.append(word)
        return ans
