from collections import Counter

# 计数+插空
# 时间复杂度O(n)，空间复杂度O(n)
# 36 ms
class Solution:
    def reorganizeString(self, S: str) -> str:
        count = Counter(S)
        if sum(count.values()) < 2 * count.most_common(1)[0][1] - 1:
            return ''
        else:
            return reorganized(count)


def reorganized(count):
    items = count.most_common()
    res = [[items[0][0]] for _ in range(items[0][1])]
    i = 0
    for k, n in items[1:]:
        for _ in range(n):
            res[i].append(k)
            i = (i + 1) % len(res)
    return ''.join(''.join(r) for r in res)
