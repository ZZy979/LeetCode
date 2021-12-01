class Solution:
    def removeDuplicates(self, S: str) -> str:
        chars = list(S)
        last_len = 99999
        while len(chars) < last_len:
            last_len = len(chars)
            i = 0
            while i < len(chars) - 1:
                if chars[i] == chars[i + 1]:
                    del chars[i:i + 2]
                else:
                    i += 1
        return ''.join(chars)
