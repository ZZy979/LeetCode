# 评论区解法，60 ms
class Solution:
    def permutation(self, s: str) -> List[str]:
        ans = ['']
        for c in s:
            ans = [word[:i] + c + word[i:] for word in ans for i in range((word + c).index(c) + 1)]
        return ans
