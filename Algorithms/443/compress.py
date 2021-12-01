class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n <= 1:
            return n
        last = None
        count = 0
        p = 0
        for q in range(n):
            if chars[q] != last:
                if last is not None:
                    chars[p] = last
                    p += 1
                if count > 1:
                    c = str(count)
                    chars[p:p + len(c)] = c
                    p += len(c)
                last = chars[q]
                count = 1
            else:
                count += 1
        chars[p] = last
        p += 1
        if count > 1:
            c = str(count)
            chars[p:p + len(c)] = c
            p += len(c)
        return p
