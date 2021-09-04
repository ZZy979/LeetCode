class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1 = [int(v) for v in v1.split('.')]
        v2 = [int(v) for v in v2.split('.')]
        if len(v1) < len(v2):
            v1 += [0] * (len(v2) - len(v1))
        else:
            v2 += [0] * (len(v1) - len(v2))
        return 1 if v1 > v2 else -1 if v1 < v2 else 0
