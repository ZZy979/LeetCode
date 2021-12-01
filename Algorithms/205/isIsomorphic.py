class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t_map = {}
        t2s_map = {}
        for i in range(len(s)):
            if s[i] not in s2t_map and t[i] not in t2s_map:
                s2t_map[s[i]] = t[i]
                t2s_map[t[i]] = s[i]
            elif s[i] in s2t_map and s2t_map[s[i]] != t[i] or t[i] in t2s_map and t2s_map[t[i]] != s[i]:
                return False
        return True
