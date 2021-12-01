class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        row = {c: r for r, s in enumerate(keyboard) for c in s}
        row.update({c.upper(): r for c, r in row.items()})
        return [word for word in words if all(row[c] == row[word[0]] for c in word)]
