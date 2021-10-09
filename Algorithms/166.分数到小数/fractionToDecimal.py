class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        neg = (numerator < 0) ^ (denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)
        
        quotient, r = divmod(numerator, denominator)
        r *= 10
        digits = []
        seen = {}
        while r != 0:
            if r in seen:
                i = seen[r]
                return '{}{:d}.{}({})'.format('-' if neg else '', quotient, ''.join(map(str, digits[:i])), ''.join(map(str, digits[i:])))
            seen[r] = len(digits)
            q, r = divmod(r, denominator)
            digits.append(q)
            r *= 10
        return '{}{:d}.{}'.format('-' if neg else '', quotient, ''.join(map(str, digits)))
