from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = defaultdict(list)
        for s in strs:
            word_map[''.join(sorted(s))].append(s)
        return list(word_map.values())
