class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        if len(S) <= 2:
            return []
        ans = []
        if backtrace(S, 0, ans) and len(ans) >= 3:
            return ans
        else:
            return []


def backtrace(s, k, seq):
    if k == len(s):
        return len(seq) >= 3
    for i in range(k + 1, len(s) + 1):
        if s[k] == '0' and i > k + 1:
            return False
        x = int(s[k:i])
        if x >= (1 << 31):
            return False
        if len(seq) < 2 or x == seq[-1] + seq[-2]:
            seq.append(x)
            if backtrace(s, i, seq):
                return True
            seq.pop()
        elif x > seq[-1] + seq[-2]:
            break
    return False
