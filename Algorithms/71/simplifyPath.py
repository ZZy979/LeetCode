class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for d in path.split('/'):
            if d not in ['', '.', '..']:
                stack.append(d)
            elif d == '..' and stack:
                stack.pop()
        return '/' + '/'.join(stack)
