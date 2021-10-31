# 评论区解法：DFS+记忆优化搜索，44 ms
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        @lru_cache
        def dfs(i, left, right, remove_left, remove_right, expr):
            if i >= len(s):
                if remove_left == remove_right == 0:
                    ans.add(expr)
                return
            if s[i] == '(':
                dfs(i + 1, left + 1, right, remove_left, remove_right, expr + s[i])
                if remove_left > 0:
                    dfs(i + 1, left, right, remove_left - 1, remove_right, expr)
            elif s[i] == ')':
                if left > right:
                    dfs(i + 1, left, right + 1, remove_left, remove_right, expr + s[i])
                if remove_right > 0:
                    dfs(i + 1, left, right, remove_left, remove_right - 1, expr)
            else:
                dfs(i + 1, left, right, remove_left, remove_right, expr + s[i])

        remove_left, remove_right = find_mismatch(s)
        ans = set()
        dfs(0, 0, 0, remove_left, remove_right, '')
        return list(ans)


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
