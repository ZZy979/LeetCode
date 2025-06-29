from collections import Counter

# 枚举+判断子序列，时间复杂度O((n/k)!*n)，空间复杂度O(C+n/k)，其中C=26
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        cnt = Counter(s)
        candidate_chars = sorted(([c, n // k] for c, n in cnt.items() if n >= k), key=lambda x: x[0], reverse=True)
        for length in range(len(s) // k, 0, -1):
            for sub_seq in generate_candidate(candidate_chars, length, []):
                if is_sub_seq(s, sub_seq * k):
                    return sub_seq
        return ''

# 按字典序降序生成候选子序列
def generate_candidate(chars, length, seq):
    if length == 0:
        yield ''.join(seq)
    else:
        for t in chars:
            if t[1] > 0:
                seq.append(t[0])
                t[1] -= 1
                yield from generate_candidate(chars, length - 1, seq)
                seq.pop()
                t[1] += 1

# 判断t是否是s的子序列
def is_sub_seq(s, t):
    n = len(s)
    i = 0
    for c in t:
        while i < n and s[i] != c:
            i += 1
        if i == n:
            return False
        i += 1
    return True
