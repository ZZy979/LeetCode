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
                    for a in str(count):
                        chars[p] = a
                        p += 1
                last = chars[q]
                count = 1
            else:
                count += 1
        chars[p] = last
        p += 1
        if count > 1:
            for a in str(count):
                chars[p] = a
                p += 1
        return p
