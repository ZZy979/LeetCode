class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if len(first) < len(second):
            first, second = second, first
        if len(first) - len(second) >= 2:
            return False
        i = 0
        while i < len(second) and first[i] == second[i]:
            i += 1
        return first[i + 1:] == second[i:] or first[i + 1:] == second[i + 1:]
