class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        p = 0
        m = min(len(s) for s in strs)
        while p < m:
            if not all(strs[i][p] == strs[0][p] for i in range(1, len(strs))):
                break
            p += 1
        return strs[0][:p]
