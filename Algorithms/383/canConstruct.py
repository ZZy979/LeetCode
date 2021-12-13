from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc, mc = Counter(ransomNote), Counter(magazine)
        return all(mc[k] >= rc[k] for k in rc)
