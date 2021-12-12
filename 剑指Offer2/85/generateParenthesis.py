class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.backtrack(n, 0, [])
        return self.ans

    def backtrack(self, n_left, n_unclosed, res):
        if n_left == 0:
            self.ans.append(''.join(res) + ')' * n_unclosed)
        else:
            res.append('(')
            self.backtrack(n_left - 1, n_unclosed + 1, res)
            res.pop()
            if n_unclosed > 0:
                res.append(')')
                self.backtrack(n_left, n_unclosed - 1, res)
                res.pop()
