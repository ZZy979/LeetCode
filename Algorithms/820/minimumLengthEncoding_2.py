# 评论区解法
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted(word[::-1] for word in words)
        return sum(len(words[i]) + 1 for i in range(len(words) - 1) if not words[i + 1].startswith(words[i])) + len(words[-1]) + 1
