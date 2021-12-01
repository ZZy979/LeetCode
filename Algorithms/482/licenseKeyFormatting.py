class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        if len(s) <= k:
            return s
        q, r = divmod(len(s), k)
        if r == 0:
            return '-'.join(s[i * k:(i + 1) * k] for i in range(q))
        else:
            return s[:r] + '-' + '-'.join(s[r + i * k: r + (i + 1) * k] for i in range(q))
