class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(v) for v in version1.split('.')]
        version2 = [int(v) for v in version2.split('.')]
        if len(version1) < len(version2):
            version1 += [0] * (len(version2) - len(version1))
        else:
            version2 += [0] * (len(version1) - len(version2))
        for i in range(len(version1)):
            if version1[i] > version2[i]:
                return 1
            elif version1[i] < version2[i]:
                return -1
        return 0
