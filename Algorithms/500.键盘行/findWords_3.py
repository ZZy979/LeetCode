# 评论区解法：子集判断
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        ans = []
        for word in words:
            s = set(word.lower())
            if any(s <= r for r in rows):
                ans.append(word)
        return ans
