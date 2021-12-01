from collections import Counter

# 回溯法，196 ms
class Solution:
    def __init__(self):
        self.ans = []

    def permutation(self, s: str) -> List[str]:
        count = Counter(s)
        self.get_perms(count, [], len(s))
        return self.ans
    
    def get_perms(self, count, prefix, remaining):
        if remaining == 0:
            self.ans.append(''.join(prefix))
            return
        for c in count:
            if count[c] > 0:
                count[c] -= 1
                prefix.append(c)
                self.get_perms(count, prefix, remaining - 1)
                prefix.pop()
                count[c] += 1
