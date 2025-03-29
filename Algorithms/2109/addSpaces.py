class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = [0] + spaces + [len(s)]
        return ' '.join(s[spaces[i]:spaces[i + 1]] for i in range(len(spaces) - 1))
