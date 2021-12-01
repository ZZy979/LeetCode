class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = 0
        m = min(len(s) for s in strs)
        while p < m and all(strs[i][p] == strs[0][p] for i in range(1, len(strs))):
            p += 1
        return strs[0][:p]
