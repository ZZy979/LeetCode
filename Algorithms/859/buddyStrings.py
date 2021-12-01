from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        cs, cg = Counter(s), Counter(goal)
        if cs != cg:
            return False
        idx = [i for i in range(len(s)) if s[i] != goal[i]]
        return len(idx) == 2 and s[idx[0]] == goal[idx[1]] and s[idx[1]] == goal[idx[0]] or not idx and any(v >= 2 for v in cs.values())
