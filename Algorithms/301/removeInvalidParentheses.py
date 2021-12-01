# 回溯，1992 ms
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left, right = find_mismatch(s)
        self.ans = set()
        self.backtrack(s, 0, 0, 0, left, right, [])
        return list(self.ans)

    def backtrack(self, s, i, mismatch_left, mismatch_right, remove_left, remove_right, expr):
        if i >= len(s):
            if mismatch_left == mismatch_right == 0:
                self.ans.add(''.join(expr))
            return
        if s[i] == '(':
            self.backtrack(s, i + 1, mismatch_left + 1, mismatch_right, remove_left, remove_right, expr + [s[i]])
            if remove_left > 0:
                self.backtrack(s, i + 1, mismatch_left, mismatch_right, remove_left - 1, remove_right, expr)
        elif s[i] == ')':
            if mismatch_left > 0:
                self.backtrack(s, i + 1, mismatch_left - 1, mismatch_right, remove_left, remove_right, expr + [s[i]])
            if remove_right > 0:
                self.backtrack(s, i + 1, mismatch_left, mismatch_right, remove_left, remove_right - 1, expr)
        else:
            self.backtrack(s, i + 1, mismatch_left, mismatch_right, remove_left, remove_right, expr + [s[i]])


def find_mismatch(s):
    left = right = 0
    for c in s:
        if c == '(':
            left += 1
        elif c == ')':
            if left > 0:
                left -= 1
            else:
                right += 1
    return left, right
