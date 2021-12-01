class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        p = i = 0
        while i < n:
            j = i + 1
            while j < n and chars[j] == chars[i]:
                j += 1
            if j - i > 1:
                chars[p] = chars[i]
                p += 1
                c = str(j - i)
                chars[p:p + len(c)] = c
                p += len(c)
            else:
                chars[p] = chars[i]
                p += 1
            i = j
        return p
