# 压缩字符串
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        compressed_name = compressed(name)
        compressed_typed = compressed(typed)
        return len(compressed_name) == len(compressed_typed) and all(
            compressed_typed[i][0] == compressed_name[i][0] and compressed_typed[i][1] >= compressed_name[i][1]
            for i in range(len(compressed_name))
        )


def compressed(s):
    if not s:
        return []
    res = []
    last = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] != last:
            res.append((last, count))
            last = s[i]
            count = 1
        else:
            count += 1
    res.append((last, count))
    return res
