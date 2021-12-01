class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.strip('/').split('/')
        s = []
        for d in dirs:
            if not d or d == '.':
                continue
            elif d == '..':
                if s:
                    s.pop()
            else:
                s.append(d)
        return '/' + '/'.join(s)
