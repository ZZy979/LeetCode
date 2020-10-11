class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        p2w_map = {}
        w2p_map = {}
        words = str.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in p2w_map and words[i] not in w2p_map:
                p2w_map[pattern[i]] = words[i]
                w2p_map[words[i]] = pattern[i]
            elif pattern[i] in p2w_map and p2w_map[pattern[i]] != words[i] or words[i] in w2p_map and w2p_map[words[i]] != pattern[i]:
                return False
        return True
