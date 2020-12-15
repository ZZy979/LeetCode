class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        digits = [int(d) for d in str(N)]
        k = 1
        while k < len(digits):
            if digits[k] < digits[k - 1]:
                break
            elif digits[k] == digits[k - 1]:
                i = k + 1
                while i < len(digits) and digits[i] == digits[k]:
                    i += 1
                if i == len(digits) or digits[i] > digits[k]:
                    # 12333 or 6666[8]841
                    k = i
                else:
                    # 1999[8]7
                    break
            else:
                k += 1
        if k == len(digits) or digits[k] == digits[k - 1] and all(digits[i] == digits[k] for i in range(k + 1, len(digits))):
            # 12345 or 12333
            return N
        else:
            # 抹零减1: 129[8]7 -> 12900 -> 12899
            return N - N % 10**(len(digits) - k) - 1
