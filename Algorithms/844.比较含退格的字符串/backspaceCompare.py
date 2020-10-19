# 模拟编辑，时间复杂度O(|S|+|T|)，空间复杂度O(|S|+|T|)
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return edit(S) == edit(T)
    
def edit(s):
    result = []
    for c in s:
        if c == '#':
            if result:
                result.pop()
        else:
            result.append(c)
    return ''.join(result)
