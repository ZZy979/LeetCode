class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return list(self.split_ip(s, 0, [], []))
    
    def split_ip(self, s, start, pos, nums):
        if len(pos) == 3:
            if pos[-1] < len(s) - 1 and s[pos[-1]] == '0':
                return
            last = int(s[pos[-1]:])
            if 0 <= last <= 255:
                yield '.'.join(map(str, nums + [last]))
        else:
            for p in range(start + 1, len(s) + len(pos) - 2):
                b = 0 if not pos else pos[-1]
                if p - b > 1 and s[b] == '0':
                    continue
                num = int(s[b:p])
                if not 0 <= num <= 255:
                    continue
                pos.append(p)
                nums.append(num)
                yield from self.split_ip(s, p, pos, nums)
                pos.pop()
                nums.pop()
