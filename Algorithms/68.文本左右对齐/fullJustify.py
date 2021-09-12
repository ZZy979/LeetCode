class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        n, i = len(words), 0
        while i < n:
            line = [words[i]]
            chars = len(words[i])
            i += 1
            while i < n and chars + len(words[i]) + len(line) - 1 < maxWidth:
                line.append(words[i])
                chars += len(words[i])
                i += 1
            if i == n or len(line) == 1:
                ans.append(' '.join(line) + ' ' * (maxWidth - chars - len(line) + 1))
            else:
                total_spaces = maxWidth - chars
                m = len(line) - 1
                k, r = divmod(total_spaces, m)
                spaces = [k + 1] * r + [k] * (m - r)
                ans.append(line[0] + ''.join(' ' * spaces[i] + line[i + 1] for i in range(m)))
        return ans
