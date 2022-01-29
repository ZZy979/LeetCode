import re

class Solution:
    def countValidWords(self, sentence: str) -> int:
        return sum(is_valid(token) for token in sentence.split())


def is_valid(token):
    return re.fullmatch(r'[a-z]*([a-z]-[a-z]+)?[!\.,]?', token) is not None
