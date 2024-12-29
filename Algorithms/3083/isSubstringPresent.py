class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        return any(s[i:i + 2][::-1] in s for i in range(len(s) - 1))
