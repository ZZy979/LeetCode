# 排序+检查每个字符串，时间复杂度O(mn²)
# 28 ms
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=len, reverse=True)
        for i in range(len(strs)):
            for j in range(len(strs)):
                if i != j and is_subsequence(strs[i], strs[j]):
                    break
            else:
                return len(strs[i])
        return -1


def is_subsequence(a, b):
    if len(a) > len(b):
        return False
    i = 0
    for j in range(len(b)):
        if i >= len(a):
            break
        if a[i] == b[j]:
            i += 1
    return i == len(a)
